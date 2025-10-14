import pytest

from libelifoot.dto.color import Color
from libelifoot.dto.equipa import Equipa
from libelifoot.dto.player import Player
from libelifoot.util.player_position import PlayerPosition


@pytest.fixture
def mock_equipa():
    player_list = [
        Player(
            name='João Ricardo',
            position=PlayerPosition.G.name,
            country='BRA'
        ),
        Player(
            name='Emanuel Brítez',
            position=PlayerPosition.D.name,
            country='ARG'
        ),
        Player(
            name='Marinho',
            position=PlayerPosition.A.name,
            country='BRA'
        ),
        Player(
            name='Yago Pikachu',
            position=PlayerPosition.A.name,
            country='BRA'
        )
    ]

    yield Equipa(
        ext_name='Fortaleza Esporte Clube',
        short_name='Fortaleza',
        country='BRA',
        level=10,
        colors=Color(text=b'001122', background=b'334455'),
        coach='Juan Pablo Vojvoda',
        players=player_list
    )


@pytest.fixture
def mock_players():
    yield [
        Player(
            name='João Ricardo',
            position=PlayerPosition.G.name,
            country='BRA'
        ),
        Player(
            name='Emanuel Brítez',
            position=PlayerPosition.D.name,
            country='ARG'
        ),
        Player(
            name='Marinho',
            position=PlayerPosition.A.name,
            country='BRA'
        ),
        Player(
            name='Yago Pikachu',
            position=PlayerPosition.A.name,
            country='BRA'
        )
    ]


@pytest.fixture
def mock_players_bytes():
    yield bytearray() # TODO
