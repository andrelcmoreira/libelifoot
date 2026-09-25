from pytest import raises
from unittest import mock
from unittest.mock import MagicMock

from fixtures import mock_players

from libelifoot.domain.entity.equipa_db_entry import Equipa
from libelifoot.domain.error.equipa_data_not_available import EquipaDataNotAvailable
from libelifoot.domain.error.equipa_not_provided import EquipaNotProvided
from libelifoot.infrastructure.provider.transfermarkt import (
    RosterProvider,
    CoachProvider
)


BASE_URL = 'https://www.transfermarkt.com.br'


def test_assemble_roster_uri_with_season_year():
    roster_prov = RosterProvider(MagicMock())
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('startseite')
    season = 2022

    uri = roster_prov.assemble_uri(team_id, season)
    assert f'{BASE_URL}/{expected_id}/saison_id/{season}' == uri


def test_assemble_roster_uri_with_no_season_year():
    roster_prov = RosterProvider(MagicMock())
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('startseite')

    uri = roster_prov.assemble_uri(team_id, 0)
    assert  f'{BASE_URL}/{expected_id}' == uri


def test_assemble_coach_uri():
    coach_prov = CoachProvider(MagicMock())
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('mitarbeiterhistorie')
    season = 2022

    uri = coach_prov.assemble_uri(team_id, season)
    assert f'{BASE_URL}/{expected_id}/personalie_id/1' == uri


def test_get_coach_with_provided_equipa():
    coach_name = 'Ralf Rangnick'
    equipa_entry = Equipa(
        id='manchester-united/mitarbeiterhistorie/verein/985',
        file='MANCITY.EFT'
    )
    season = 2022
    repo_mock = MagicMock()
    coach_prov = CoachProvider(repo_mock)

    repo_mock.get_team.return_value = equipa_entry

    with mock.patch.object(
        CoachProvider,
        '_fetch_data',
        return_value=coach_name
    ) as mock_fetch_data:
        name = coach_prov.get_coach(equipa_entry.file, season)

        assert name == coach_name

        repo_mock.get_team.assert_called_once_with(
            equipa_entry.file,
            coach_prov.name
        )
        mock_fetch_data.assert_called_once_with(equipa_entry.id, season)


def test_get_coach_with_no_provided_equipa():
    equipa_entry = Equipa(
        id='manchester-united/mitarbeiterhistorie/verein/985',
        file='MANCITY.EFT'
    )
    season = 2022
    repo_mock = MagicMock()
    coach_prov = CoachProvider(repo_mock)

    repo_mock.get_team.return_value = None
    with raises(EquipaNotProvided):
        coach_prov.get_coach(equipa_entry.file, season)

    repo_mock.get_team.assert_called_once_with(
        equipa_entry.file,
        coach_prov.name
    )


def test_get_players_with_no_provided_equipa():
    equipa_entry = Equipa(
        id='manchester-united/mitarbeiterhistorie/verein/985',
        file='MANCITY.EFT'
    )
    season = 2022
    repo_mock = MagicMock()
    roster_prov = RosterProvider(repo_mock)

    repo_mock.get_team.return_value = None

    with raises(EquipaNotProvided):
        roster_prov.get_players(equipa_entry.file, season)

    repo_mock.get_team.assert_called_once_with(
        equipa_entry.file,
        roster_prov.name
    )


def test_get_players_with_no_data_available():
    equipa_entry = Equipa(
        id='manchester-united/mitarbeiterhistorie/verein/985',
        file='MANCITY.EFT'
    )
    season = 2022
    repo_mock = MagicMock()
    roster_prov = RosterProvider(repo_mock)

    repo_mock.get_team.return_value = equipa_entry

    with mock.patch.object(
        roster_prov,
        '_fetch_data',
        return_value=[]
    ) as mock_fetch_team_data:
        with raises(EquipaDataNotAvailable):
            roster_prov.get_players(equipa_entry.file, season)

        repo_mock.get_team.assert_called_once_with(
            equipa_entry.file,
            roster_prov.name
        )
        mock_fetch_team_data.assert_called_once_with(equipa_entry.id, season)


def test_get_players_with_data_available(mock_players):
    equipa_entry = Equipa(
        id='manchester-united/mitarbeiterhistorie/verein/985',
        file='MANCITY.EFT'
    )
    season = 2022
    repo_mock = MagicMock()
    roster_prov = RosterProvider(repo_mock)

    repo_mock.get_team.return_value = equipa_entry

    with (
        mock.patch.object(
            roster_prov,
            '_fetch_data',
            return_value=mock_players
        ) as mock_fetch_data,
        mock.patch(
            'libelifoot.infrastructure.provider.transfermarkt.RosterProvider.select_players',
            return_value=mock_players
        ) as mock_select_players,
    ):
        players = roster_prov.get_players(equipa_entry.file, season)

        assert players == mock_players

        repo_mock.get_team.assert_called_once_with(
            equipa_entry.file,
            roster_prov.name
        )
        mock_fetch_data.assert_called_once_with(equipa_entry.id, season)
        mock_select_players.assert_called_once_with(mock_players)
