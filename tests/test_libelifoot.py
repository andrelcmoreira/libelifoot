from unittest import mock

from fixtures import mock_equipa

from libelifoot import (
    bulk_update,
    get_providers,
    get_equipa_data,
    update_equipa
)


def test_update_equipa():
    equipa_file = 'FORTALEZA.EFT'
    provider = 'espn'
    season = 2024
    listener = mock.MagicMock()

    with mock.patch(
        'libelifoot.use_case.update_equipa.Cmd.run'
    ) as cmd_mock:
        update_equipa(equipa_file, provider, season, listener)

        cmd_mock.assert_called_once()


def test_bulk_update_equipa():
    equipa_dir = 'foo/bar'
    provider = 'espn'
    season = 2024
    listener = mock.MagicMock()

    with mock.patch(
        'libelifoot.use_case.bulk_update.Cmd.run'
    ) as cmd_mock:
        bulk_update(equipa_dir, provider, season, listener)

        cmd_mock.assert_called_once()


def test_get_equipa_data(mock_equipa):
    equipa_file = 'FORTALEZA.EFT'

    with mock.patch(
        'libelifoot.use_case.get_equipa_data.Cmd.run',
        return_value=mock_equipa
    ) as cmd_mock:
        equipa = get_equipa_data(equipa_file)

        cmd_mock.assert_called_once()
        assert equipa == mock_equipa


def test_get_providers():
    fake_providers = ['provider-1', 'provider-2', 'provider-3']

    with mock.patch(
        'libelifoot.use_case.get_providers.Cmd.run',
        return_value=fake_providers
    ) as cmd_mock:
        providers = get_providers()

        cmd_mock.assert_called_once()
        assert providers == fake_providers
