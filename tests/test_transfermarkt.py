from pytest import raises
from unittest import mock

from fixtures import mock_players

from libelifoot.error.not_provided import EquipaNotProvided
from libelifoot.error.data_not_available import EquipaDataNotAvailable
from libelifoot.provider.transfermarkt import RosterProvider, CoachProvider


ROSTER_PROV = RosterProvider()
BASE_URL = 'https://www.transfermarkt.com.br'


def test_assemble_roster_uri_with_season_year():
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('startseite')
    season = 2022

    uri = ROSTER_PROV.assemble_uri(team_id, season)
    assert f'{BASE_URL}/{expected_id}/saison_id/{season}' == uri


def test_assemble_roster_uri_with_no_season_year():
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('startseite')

    uri = ROSTER_PROV.assemble_uri(team_id, 0)
    assert  f'{BASE_URL}/{expected_id}' == uri


def test_assemble_coach_uri():
    coach_prov = CoachProvider()
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('mitarbeiterhistorie')
    season = 2022

    uri = coach_prov.assemble_uri(team_id, season)
    assert f'{BASE_URL}/{expected_id}/personalie_id/1' == uri


def test_get_coach_with_provided_equipa():
    team_id = 'manchester-united/mitarbeiterhistorie/verein/985'
    coach_name = 'Ralf Rangnick'
    season = 2022
    coach_prov = CoachProvider()

    with (
        mock.patch(
            'libelifoot.equipa.mapping.get_team_id',
            return_value=team_id
        ) as mock_get_team_id,
        mock.patch.object(
            CoachProvider,
            '_fetch_coach_data',
            return_value=coach_name
        ) as mock_fetch_coach_data,
    ):
        name = coach_prov.get_coach(team_id, season)

        assert name == coach_name

        mock_get_team_id.assert_called_once_with(team_id, coach_prov.name)
        mock_fetch_coach_data.assert_called_once_with(team_id, season)


def test_get_coach_with_no_provided_equipa():
    team_id = 'FORTALEZA.EFT'
    season = 2022
    coach_prov = CoachProvider()

    with mock.patch(
        'libelifoot.equipa.mapping.get_team_id',
        return_value=''
    ) as mock_get_team_id:
        with raises(EquipaNotProvided):
            coach_prov.get_coach(team_id, season)

        mock_get_team_id.assert_called_once_with(team_id, coach_prov.name)


def test_get_players_with_no_provided_equipa():
    team_id = 'FORTALEZA.EFT'
    season = 2022

    with mock.patch(
        'libelifoot.equipa.mapping.get_team_id',
        return_value=''
    ) as mock_get_team_id:
        with raises(EquipaNotProvided):
            ROSTER_PROV.get_players(team_id, season)

        mock_get_team_id.assert_called_once_with(team_id, ROSTER_PROV.name)


def test_get_players_with_no_data_available():
    team_id = 'manchester-united/mitarbeiterhistorie/verein/985'
    season = 2022

    with (
        mock.patch(
            'libelifoot.equipa.mapping.get_team_id',
            return_value=team_id
        ) as mock_get_team_id,
        mock.patch.object(
            ROSTER_PROV,
            '_fetch_team_data',
            return_value=[]
        ) as mock_fetch_team_data,
    ):
        with raises(EquipaDataNotAvailable):
            ROSTER_PROV.get_players(team_id, season)

        mock_get_team_id.assert_called_once_with(team_id, ROSTER_PROV.name)
        mock_fetch_team_data.assert_called_once_with(team_id, season)


def test_get_players_with_data_available(mock_players):
    team_id = 'manchester-united/mitarbeiterhistorie/verein/985'
    season = 2022

    with (
        mock.patch(
            'libelifoot.equipa.mapping.get_team_id',
            return_value=team_id
        ) as mock_get_team_id,
        mock.patch.object(
            ROSTER_PROV,
            '_fetch_team_data',
            return_value=mock_players
        ) as mock_fetch_team_data,
        mock.patch(
            'libelifoot.provider.transfermarkt.RosterProvider.select_players',
            return_value=mock_players
        ) as mock_select_players,
    ):
        players = ROSTER_PROV.get_players(team_id, season)

        assert players == mock_players

        mock_get_team_id.assert_called_once_with(team_id, ROSTER_PROV.name)
        mock_fetch_team_data.assert_called_once_with(team_id, season)
        mock_select_players.assert_called_once_with(mock_players)
