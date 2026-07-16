from unittest.mock import patch

from libelifoot.use_case import get_providers


def test_get_equipa_data():
    fake_providers = ['provider-1', 'provider-2', 'provider-3']

    with patch(
        'libelifoot.provider.db.get_providers',
        return_value=fake_providers
    ) as mock_get:
        cmd = get_providers.Cmd()

        assert cmd.run() == fake_providers
        mock_get.assert_called_once_with()
