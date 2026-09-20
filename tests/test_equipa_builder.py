from unittest.mock import patch, MagicMock
from pytest import raises

from fixtures import mock_equipa, mock_players, mock_equipa_bytes

from libelifoot.domain.error.equipa_not_found import EquipaNotFound
from libelifoot.use_case.update_equipa import UpdateEquipa
from libelifoot.use_case.dto.equipa import Equipa


def test_create_base_equipa_with_not_existent_file():
    equipa_file = 'NOT_EXISTENT.eft'
    repo_mock = MagicMock()
    builder = UpdateEquipa.Builder(repo_mock)

    repo_mock.get.return_value = None

    with raises(EquipaNotFound, match=f"Equipa '{equipa_file}' not found!"):
        builder.create_base_equipa(equipa_file)


def test_create_base_equipa_with_existent_file(mock_equipa, mock_equipa_bytes):
    equipa_file = 'FORTALEZA.eft'
    repo_mock = MagicMock()
    builder = UpdateEquipa.Builder(repo_mock)
    equipa_dto_mock = Equipa.from_entity(mock_equipa)

    repo_mock.get.return_value = mock_equipa_bytes

    with patch(
        'libelifoot.use_case.dto.equipa.Equipa.from_entity',
        return_value=equipa_dto_mock
    ) as from_entity_mock:
        builder.create_base_equipa(equipa_file)

        repo_mock.get.assert_called_with(equipa_file)
        from_entity_mock.assert_called_with(mock_equipa)


def test_add_players_to_equipa(mock_equipa, mock_equipa_bytes, mock_players):
    equipa_file = 'FORTALEZA.eft'
    repo_mock = MagicMock()
    builder = UpdateEquipa.Builder(repo_mock)
    equipa_dto_mock = Equipa.from_entity(mock_equipa)

    repo_mock.get.return_value = mock_equipa_bytes

    with patch(
        'libelifoot.use_case.dto.equipa.Equipa.from_entity',
        return_value=equipa_dto_mock
    ) as from_entity_mock:
        builder.create_base_equipa(equipa_file)

        builder.add_players(mock_players)
        equipa = builder.build()

        assert equipa.players == mock_players

        repo_mock.get.assert_called_with(equipa_file)
        from_entity_mock.assert_called_with(mock_equipa)


def test_add_coach_to_equipa(mock_equipa, mock_equipa_bytes):
    equipa_file = 'FORTALEZA.eft'
    repo_mock = MagicMock()
    builder = UpdateEquipa.Builder(repo_mock)
    equipa_dto_mock = Equipa.from_entity(mock_equipa)

    repo_mock.get.return_value = mock_equipa_bytes

    with patch(
        'libelifoot.use_case.dto.equipa.Equipa.from_entity',
        return_value=equipa_dto_mock
    ) as from_entity_mock:
        builder.create_base_equipa(equipa_file)

        builder.add_coach(mock_equipa.coach)
        equipa = builder.build()

        assert equipa.coach == mock_equipa.coach

        repo_mock.get.assert_called_with(equipa_file)
        from_entity_mock.assert_called_with(mock_equipa)


def test_add_coach_with_empty_name(mock_equipa, mock_equipa_bytes):
    equipa_file = 'FORTALEZA.eft'
    repo_mock = MagicMock()
    builder = UpdateEquipa.Builder(repo_mock)
    equipa_dto_mock = Equipa.from_entity(mock_equipa)

    repo_mock.get.return_value = mock_equipa_bytes

    with patch(
        'libelifoot.use_case.dto.equipa.Equipa.from_entity',
        return_value=equipa_dto_mock
    ) as from_entity_mock:
        builder.create_base_equipa(equipa_file)

        builder.add_coach('')
        equipa = builder.build()

        assert equipa.coach == mock_equipa.coach

        repo_mock.get.assert_called_with(equipa_file)
        from_entity_mock.assert_called_with(mock_equipa)


def test_add_players_without_base_equipa(mock_players):
    builder = UpdateEquipa.Builder(MagicMock())

    builder.add_players(mock_players)
    equipa = builder.build()

    assert equipa is None


def test_add_coach_without_base_equipa():
    coach = 'Juan Pablo Vojvoda'
    builder = UpdateEquipa.Builder(MagicMock())

    builder.add_coach(coach)
    equipa = builder.build()

    assert equipa is None
