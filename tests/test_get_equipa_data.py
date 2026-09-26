from unittest.mock import MagicMock
from pytest import raises

from fixtures import mock_equipa_bytes, mock_equipa

from libelifoot.domain.error.equipa_not_found import EquipaNotFound
from libelifoot.use_case.dto.equipa import Equipa
from libelifoot.use_case.get_equipa_data import GetEquipaData


def test_get_equipa_data_with_not_found_equipa():
    file = 'FORTALEZA.EFT'
    repo_mock = MagicMock()

    repo_mock.get.return_value = None

    cmd = GetEquipaData(file, repo_mock)
    with raises(EquipaNotFound):
        cmd.run()


def test_get_equipa_data_with_valid_equipa(mock_equipa, mock_equipa_bytes):
    file = 'FORTALEZA.EFT'
    repo_mock = MagicMock()

    repo_mock.get.return_value = mock_equipa_bytes

    cmd = GetEquipaData(file, repo_mock)
    ret = cmd.run()

    assert ret == Equipa.from_entity(mock_equipa)
