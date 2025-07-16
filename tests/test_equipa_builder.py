from unittest.mock import patch
from pytest import raises

from libelifoot.entity.color import Color
from libelifoot.entity.equipa import Equipa
from libelifoot.entity.player import Player
from libelifoot.util.player_position import PlayerPosition
from libelifoot.equipa.builder import EquipaBuilder
from libelifoot.error.not_found import EquipaNotFound


def test_create_base_equipa_with_not_existent_file():
    equipa_file = 'NOT_EXISTENT.eft'
    builder = EquipaBuilder()

    with raises(EquipaNotFound, match=f"Equipa '{equipa_file}' not found!"):
        builder.create_base_equipa(equipa_file)


@patch('libelifoot.file.equipa.EquipaFileHandler.read')
def test_create_base_equipa_with_existent_file(read_mock):
    builder = EquipaBuilder()
    equipa_file = 'FORTALEZA.eft'
    player_list = [
        Player(name='João Ricardo', position=PlayerPosition.G.name,
               country='BRA'),
        Player(name='Emanuel Brítez', position=PlayerPosition.D.name,
               country='ARG'),
        Player(name='Marinho', position=PlayerPosition.A.name, country='BRA'),
        Player(name='Yago Pikachu', position=PlayerPosition.A.name,
               country='BRA')
    ]
    equipa = Equipa(ext_name='Fortaleza Esporte Clube', short_name='Fortaleza',
                    country='BRA', level=10,
                    colors=Color(text=b'', background=b''),
                    coach='Juan Pablo Vojvoda', players=player_list)

    read_mock.return_value = equipa

    builder.create_base_equipa(equipa_file)

    read_mock.assert_called_with(equipa_file)
