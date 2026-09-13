from unittest import mock
from unittest.mock import MagicMock

from fixtures import mock_roster_provider

from libelifoot.domain.entity.equipa_db_entry import EquipaDbEntry
from libelifoot.use_case.bulk_update import BulkUpdate


def test_bulk_update(mock_roster_provider):
    equipa_dir = 'foo/bar/equipas'
    season = 2024
    teams = [
        EquipaDbEntry(id='1', file='TEAM1.EFT'),
        EquipaDbEntry(id='2', file='TEAM2.EFT'),
        EquipaDbEntry(id='3', file='TEAM3.EFT')
    ]

    mock_team_repo = MagicMock()
    mock_equipa_repo = MagicMock()
    mock_coach_provider = MagicMock()
    mock_listener = MagicMock()

    mock_team_repo.get_teams.return_value = teams

    with mock.patch(
        'libelifoot.use_case.update_equipa.UpdateEquipa'
    ) as mock_update_equipa:
        cmd = BulkUpdate(
            equipa_dir,
            mock_roster_provider,
            mock_coach_provider,
            season,
            mock_team_repo,
            mock_equipa_repo,
            mock_listener
        )
        cmd.run()

        mock_team_repo.get_teams.assert_called_once_with(mock_roster_provider.name)
        mock_update_equipa.assert_has_calls([
            mock.call(
                f"{equipa_dir}/{teams[0].file}",
                mock_roster_provider,
                mock_coach_provider,
                season,
                mock_equipa_repo,
                mock_listener
            ),
            mock.call().run(),
            mock.call(
                f"{equipa_dir}/{teams[1].file}",
                mock_roster_provider,
                mock_coach_provider,
                season,
                mock_equipa_repo,
                mock_listener
            ),
            mock.call().run(),
            mock.call(
                f"{equipa_dir}/{teams[2].file}",
                mock_roster_provider,
                mock_coach_provider,
                season,
                mock_equipa_repo,
                mock_listener
            ),
            mock.call().run()
        ])
        assert mock_update_equipa.call_count == len(teams)


def test_bulk_update_with_no_teams(mock_roster_provider):
    equipa_dir = 'foo/bar/equipas'
    season = 2024

    mock_team_repo = MagicMock()
    mock_equipa_repo = MagicMock()
    mock_coach_provider = MagicMock()
    mock_listener = MagicMock()

    mock_team_repo.get_teams.return_value = []

    with mock.patch(
        'libelifoot.use_case.update_equipa.UpdateEquipa'
    ) as mock_update_equipa:
        cmd = BulkUpdate(
            equipa_dir,
            mock_roster_provider,
            mock_coach_provider,
            season,
            mock_team_repo,
            mock_equipa_repo,
            mock_listener
        )
        cmd.run()

        mock_team_repo.get_teams.assert_called_once_with(mock_roster_provider.name)
        mock_update_equipa.assert_not_called()
