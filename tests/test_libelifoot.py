from unittest import mock

from fixtures import mock_equipa

from libelifoot import bulk_update, update_equipa, view_equipa


def test_update_equipa():
    equipa_file = 'FORTALEZA.EFT'
    provider = 'espn'
    season = 2024
    listener = mock.MagicMock()

    with mock.patch(
        'libelifoot.api.update_equipa.Cmd.run'
    ) as cmd_mock:
        update_equipa(equipa_file, provider, season, listener)

        cmd_mock.assert_called_once()


def test_bulk_update_equipa():
    equipa_dir = 'foo/bar'
    provider = 'espn'
    season = 2024
    listener = mock.MagicMock()

    with mock.patch(
        'libelifoot.api.bulk_update.Cmd.run'
    ) as cmd_mock:
        bulk_update(equipa_dir, provider, season, listener)

        cmd_mock.assert_called_once()


def test_view_equipa(mock_equipa):
    equipa_file = 'FORTALEZA.EFT'

    with mock.patch(
        'libelifoot.api.view_equipa.view',
        return_value=mock_equipa
    ) as view_mock:
        equipa = view_equipa(equipa_file)

        view_mock.assert_called_once_with(equipa_file)
        assert equipa == mock_equipa
