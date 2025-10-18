from unittest.mock import patch
from pytest import raises

from fixtures import mock_equipa, mock_players

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


def test_add_players_to_equipa(mock_equipa, mock_players):
    equipa_file = 'FORTALEZA.eft'
    builder = EquipaBuilder()

    with patch(
        'libelifoot.file.equipa.EquipaFileHandler.read',
        return_value=mock_equipa
    ) as read_mock:
        builder.create_base_equipa(equipa_file)

        builder.add_players(mock_players)
        equipa = builder.build()

        assert equipa.players == mock_players

        read_mock.assert_called_with(equipa_file)


def test_add_coach_to_equipa(mock_equipa):
    equipa_file = 'FORTALEZA.eft'
    coach = 'Juan Pablo Vojvoda'
    builder = EquipaBuilder()

    with patch(
        'libelifoot.file.equipa.EquipaFileHandler.read',
        return_value=mock_equipa
    ) as read_mock:
        builder.create_base_equipa(equipa_file)

        builder.add_coach(coach)
        equipa = builder.build()

        assert equipa.coach == coach

        read_mock.assert_called_with(equipa_file)


def test_add_coach_with_empty_name(mock_equipa):
    equipa_file = 'FORTALEZA.eft'
    builder = EquipaBuilder()

    with patch(
        'libelifoot.file.equipa.EquipaFileHandler.read',
        return_value=mock_equipa
    ) as read_mock:
        builder.create_base_equipa(equipa_file)

        builder.add_coach('')
        equipa = builder.build()

        assert equipa.coach == mock_equipa.coach

        read_mock.assert_called_with(equipa_file)


def test_add_players_without_base_equipa(mock_players):
    builder = EquipaBuilder()

    builder.add_players(mock_players)
    equipa = builder.build()

    assert equipa is None


def test_add_coach_without_base_equipa():
    coach = 'Juan Pablo Vojvoda'
    builder = EquipaBuilder()

    builder.add_coach(coach)
    equipa = builder.build()

    assert equipa is None
