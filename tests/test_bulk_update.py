from unittest import mock

from libelifoot.api import bulk_update
from fixtures import mock_roster_provider


@mock.patch('libelifoot.equipa.mapping.get_teams')
def test_bulk_update(mock_get_teams, mock_roster_provider):
    equipa_dir = 'foo/bar/equipas'
    season = 2024
    teams = [
        {'id': '1', 'file': 'TEAM1.EFT'},
        {'id': '2', 'file': 'TEAM2.EFT'},
        {'id': '3', 'file': 'TEAM3.EFT'},
    ]

    mock_get_teams.return_value = teams
    mock_coach_provider = mock.MagicMock()
    mock_listener = mock.MagicMock()

    with mock.patch(
        'libelifoot.api.update_equipa.Cmd'
    ) as mock_update_equipa:
        cmd = bulk_update.Cmd(equipa_dir, mock_roster_provider,
                              mock_coach_provider, season, mock_listener)
        cmd.run()

        mock_get_teams.assert_called_once_with(mock_roster_provider.name)
        mock_update_equipa.assert_has_calls([
            mock.call(f"{equipa_dir}/{teams[0]['file']}", mock_roster_provider,
                      mock_coach_provider, season, mock_listener),
            mock.call().run(),
            mock.call(f"{equipa_dir}/{teams[1]['file']}", mock_roster_provider,
                      mock_coach_provider, season, mock_listener),
            mock.call().run(),
            mock.call(f"{equipa_dir}/{teams[2]['file']}", mock_roster_provider,
                      mock_coach_provider, season, mock_listener),
            mock.call().run()
        ])
        assert mock_update_equipa.call_count == len(teams)


@mock.patch('libelifoot.equipa.mapping.get_teams')
def test_bulk_update_with_no_teams(mock_get_teams, mock_roster_provider):
    equipa_dir = 'foo/bar/equipas'
    season = 2024

    mock_get_teams.return_value = []
    mock_coach_provider = mock.MagicMock()
    mock_listener = mock.MagicMock()

    with mock.patch(
        'libelifoot.api.update_equipa.Cmd'
    ) as mock_update_equipa:
        cmd = bulk_update.Cmd(equipa_dir, mock_roster_provider,
                              mock_coach_provider, season, mock_listener)
        cmd.run()

        mock_get_teams.assert_called_once_with(mock_roster_provider.name)
        mock_update_equipa.assert_not_called()
