from unittest import mock

from fixtures import mock_equipa, mock_players
from libelifoot.api import update_equipa
from libelifoot.error.data_not_available import EquipaDataNotAvailable
from libelifoot.error.not_found import EquipaNotFound
from libelifoot.error.not_provided import EquipaNotProvided


@mock.patch('libelifoot.provider.base_roster_provider')
@mock.patch('libelifoot.provider.base_coach_provider')
@mock.patch('libelifoot.event.update_equipa_listener.UpdateEquipaListener')
def test_update_equipa(mock_listener, mock_coach_prov, mock_roster_prov,
                       mock_equipa, mock_players):
    equipa_file = 'FORTALEZA.EFT'
    coach = 'Juan Pablo Vojvoda'
    season = 2024

    mock_roster_prov.get_players.return_value = mock_players
    mock_coach_prov.get_coach.return_value = coach

    with mock.patch(
        'libelifoot.equipa.builder.EquipaBuilder',
        return_value=mock.MagicMock()
    ) as mock_builder:
        mock_builder \
            .return_value \
            .create_base_equipa \
            .return_value \
            .add_players \
            .return_value \
            .add_coach \
            .return_value  \
            .build \
            .return_value = mock_equipa

        cmd = update_equipa.Cmd(equipa_file, mock_roster_prov, mock_coach_prov,
                                season, mock_listener)
        cmd.run()

        mock_roster_prov.get_players.assert_called_once_with(equipa_file, season)
        mock_coach_prov.get_coach.assert_called_once_with(equipa_file, season)
        mock_builder.assert_called_once()
        # TODO: improve the code below
        mock_builder \
            .return_value \
            .create_base_equipa \
            .assert_called_once_with(equipa_file)
        mock_builder \
            .return_value \
            .create_base_equipa \
            .return_value \
            .add_players \
            .assert_called_once_with(mock_players)
        mock_builder \
            .return_value \
            .create_base_equipa \
            .return_value \
            .add_players \
            .return_value \
            .add_coach \
            .assert_called_once_with(coach)
        mock_builder \
            .return_value \
            .create_base_equipa \
            .return_value \
            .add_players \
            .return_value \
            .add_coach \
            .return_value \
            .build.assert_called_once()
        mock_listener.on_update_equipa.assert_called_once_with(equipa_file,
                                                               mock_equipa)


@mock.patch('libelifoot.provider.base_roster_provider')
@mock.patch('libelifoot.provider.base_coach_provider')
@mock.patch('libelifoot.event.update_equipa_listener.UpdateEquipaListener')
def test_update_equipa_not_found(mock_listener, mock_coach_prov,
                                  mock_roster_prov):
    equipa_file = 'NON_EXISTENT.EFT'
    season = 2024
    expected_error = f"Equipa '{equipa_file}' not found!"

    mock_roster_prov.get_players.side_effect = EquipaNotFound(equipa_file)
    cmd = update_equipa.Cmd(equipa_file, mock_roster_prov, mock_coach_prov,
                            season, mock_listener)
    cmd.run()

    mock_roster_prov.get_players.assert_called_once_with(equipa_file, season)
    mock_listener.on_update_equipa_error.assert_called_once_with(expected_error)


@mock.patch('libelifoot.provider.base_roster_provider')
@mock.patch('libelifoot.provider.base_coach_provider')
@mock.patch('libelifoot.event.update_equipa_listener.UpdateEquipaListener')
def test_update_equipa_with_no_data_available(mock_listener, mock_coach_prov,
                                              mock_roster_prov):
    equipa_file = 'EXISTENT.EFT'
    season = 2024
    expected_error = f"The specified provider has no data for equipa '{equipa_file}'!"

    mock_roster_prov.get_players.side_effect = EquipaDataNotAvailable(equipa_file)
    cmd = update_equipa.Cmd(equipa_file, mock_roster_prov, mock_coach_prov,
                            season, mock_listener)
    cmd.run()

    mock_roster_prov.get_players.assert_called_once_with(equipa_file, season)
    mock_listener.on_update_equipa_error.assert_called_once_with(expected_error)


@mock.patch('libelifoot.provider.base_roster_provider')
@mock.patch('libelifoot.provider.base_coach_provider')
@mock.patch('libelifoot.event.update_equipa_listener.UpdateEquipaListener')
def test_update_equipa_with_no_header(mock_listener, mock_coach_prov,
                                      mock_roster_prov):
    equipa_file = 'EXISTENT.EFT'
    season = 2024
    expected_error = f"Equipa '{equipa_file}' not available by the specified provider!"

    mock_roster_prov.get_players.side_effect = EquipaNotProvided(equipa_file)
    cmd = update_equipa.Cmd(equipa_file, mock_roster_prov, mock_coach_prov,
                            season, mock_listener)
    cmd.run()

    mock_roster_prov.get_players.assert_called_once_with(equipa_file, season)
    mock_listener.on_update_equipa_error.assert_called_once_with(expected_error)
