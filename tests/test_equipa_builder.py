from unittest.mock import patch
from pytest import raises

from fixtures import mock_equipa

from libelifoot.equipa.builder import EquipaBuilder
from libelifoot.error.not_found import EquipaNotFound


def test_create_base_equipa_with_not_existent_file():
    equipa_file = 'NOT_EXISTENT.eft'
    builder = EquipaBuilder()

    with raises(EquipaNotFound, match=f"Equipa '{equipa_file}' not found!"):
        builder.create_base_equipa(equipa_file)


def test_create_base_equipa_with_existent_file(mock_equipa):
    equipa_file = 'FORTALEZA.eft'
    builder = EquipaBuilder()

    with patch(
        'libelifoot.file.equipa.EquipaFileHandler.read',
        return_value=mock_equipa
    ) as read_mock:
        builder.create_base_equipa(equipa_file)

        read_mock.assert_called_with(equipa_file)
