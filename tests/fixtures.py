import pytest

from libelifoot.entity.color import Color
from libelifoot.entity.equipa import Equipa
from libelifoot.entity.player import Player
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
def mock_equipa_bytes():
    yield bytearray(
        b"EFa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17]\xcc>"
        b"\xb2\x13\x7f\xe4^\xbf\xdf$\x97\x07v\xe8\\\xc1\xe1$\x90\x05g\xcc\tO"
        b"\xbe0\xa4\x05q\xd6P\xb1334455\x00001122\x00\x03E\x97\xd8\n\x04\x00"
        b"\x03E\x97\xd8\x0cV\xc5\xa8\x177\x89\xf2U\xb6(\x8c\xfb\x00\x00\x03D"
        b"\x96\xdd\x0eS\xc0!\x8f\x04i\xd5\xf57\xa9\x96\no\xe9\x01\x00\x03E\x97"
        b"\xd8\x07T\xb5\'\x90\xfef\xd5\x03\x00\x03E\x97\xd8\x0ce\xc6-\x9c\xbc"
        b"\x0cu\xe0A\xa4\x0c\x81\x03\x00\x12\\\xd12\xa0\xc0\x10q\xd3?\xae\xce$"
        b"\x93\xfds\xe2F\xa7"
    )
