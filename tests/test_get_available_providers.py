from unittest.mock import MagicMock

from libelifoot.domain.entity.provider import Provider
from libelifoot.use_case.get_providers import GetProviders


def test_get_equipa_data():
    fake_providers = [
        Provider(name='provider-1', url=''),
        Provider(name='provider-2', url=''),
        Provider(name='provider-3', url='')
    ]
    expcted_result = [
        fake_providers[0].name,
        fake_providers[1].name,
        fake_providers[2].name
    ]
    repo_mock = MagicMock()
    cmd = GetProviders(repo_mock)

    repo_mock.get_providers.return_value = fake_providers

    assert cmd.run() == expcted_result
    repo_mock.get_providers.assert_called_once_with()
