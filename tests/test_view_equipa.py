from unittest.mock import patch

from libelifoot.api.view_equipa import view
from libelifoot.dto.color import Color
from libelifoot.dto.equipa import Equipa
from libelifoot.dto.player import Player
from libelifoot.util.player_position import PlayerPosition


@patch('libelifoot.file.equipa.EquipaFileHandler.read')
def test_view_equipa(mock_read):
    file = 'FORTALEZA.EFT'
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

    mock_read.return_value = equipa

    assert view(file) == equipa

    mock_read.assert_called_once_with(file)
