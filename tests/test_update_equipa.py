from unittest import mock

from fixtures import mock_equipa, mock_players
from libelifoot.api import update_equipa


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
