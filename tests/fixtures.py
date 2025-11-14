import pytest

from libelifoot.entity.color import Color
from libelifoot.entity.equipa import Equipa
from libelifoot.entity.player import Player
from libelifoot.util.player_position import PlayerPosition


@pytest.fixture
def mock_equipa():
    player_list = [
        Player(
            name='Agustín Rossi',
            position=PlayerPosition.G.name,
            country='ARG',
            appearances=0,
            value=0.0
        ),
        Player(
            name='M Queiroz',
            position=PlayerPosition.G.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Lucas Furtado',
            position=PlayerPosition.G.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Ayrton Lucas',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Wesley França',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Léo Pereira',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Fabrício Bruno',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Léo Ortiz',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='David Luiz',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Gerson',
            position=PlayerPosition.M.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Allan',
            position=PlayerPosition.M.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Erick Pulgar',
            position=PlayerPosition.M.name,
            country='CHL',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Lorran Lucas ',
            position=PlayerPosition.M.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Evertton',
            position=PlayerPosition.M.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='G de Arrascaeta',
            position=PlayerPosition.M.name,
            country='URU',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Bruno Henrique',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Luiz Araújo',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Pedro',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Gabriel Barbosa',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Matheus Gonçalves',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Carlinhos',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        )
    ]

    yield Equipa(
        ext_name='CR FLAMENGO',
        short_name='FLAMENGO',
        country='BRA',
        level=14,
        colors=Color(text=b'000000', background=b'FF0000'),
        coach='Filipe Luís',
        players=player_list
    )


@pytest.fixture
def mock_players():
    yield [
        Player(
            name='Agustín Rossi',
            position=PlayerPosition.G.name,
            country='ARG',
            appearances=0,
            value=0.0
        ),
        Player(
            name='M Queiroz',
            position=PlayerPosition.G.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Lucas Furtado',
            position=PlayerPosition.G.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Ayrton Lucas',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Wesley França',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Léo Pereira',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Fabrício Bruno',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Léo Ortiz',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='David Luiz',
            position=PlayerPosition.D.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Gerson',
            position=PlayerPosition.M.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Allan',
            position=PlayerPosition.M.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Erick Pulgar',
            position=PlayerPosition.M.name,
            country='CHL',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Lorran Lucas ',
            position=PlayerPosition.M.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Evertton',
            position=PlayerPosition.M.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='G de Arrascaeta',
            position=PlayerPosition.M.name,
            country='URU',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Bruno Henrique',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Luiz Araújo',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Pedro',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Gabriel Barbosa',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Matheus Gonçalves',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        ),
        Player(
            name='Carlinhos',
            position=PlayerPosition.A.name,
            country='BRA',
            appearances=0,
            value=0.0
        )
    ]


@pytest.fixture
def mock_equipa_bytes():
    yield bytearray(
        b"EFa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0bN\xa0\xc0"
        b"\x06R\x93\xe0%s\xba\t\x08N\x9a\xdb(m\xbb\x02Q\x00\x00\x00\x00\xff\x00"
        b"\x00\x00\x03E\x97\xd8\x0e\x15\x00\x03D\x96\xdd\rN\xb5*\x9d\x11\xfel"
        b"\x8c\xdeM\xc03\x9c\x00\x00\x03E\x97\xd8\tVv\xc7<\xa1\n|\xebe\x00\x00"
        b"\x03E\x97\xd8\rY\xce1\x92\x05%k\xe0R\xc6'\x8b\xfa\x00\x00\x03E\x97"
        b"\xd8\x0cM\xc68\xac\x1b\x89\xa9\xf5j\xcd.\xa1\x01\x00\x03E\x97\xd8\rd"
        b"\xc9<\xa8\r\x86\xa6\xec^\xbf-\x14u\x01\x00\x03E\x97\xd8\x0bW@\xaf\xcf"
        b"\x1f\x84\xf6[\xc46\x97\x01\x00\x03E\x97\xd8\x0eT\xb5\x17\x89v\xd9B"
        b"\xb1\xd1\x13\x85\xfah\xd7\x01\x00\x03E\x97\xd8\tU>\xad\xcd\x1c\x8e"
        b"\x02k\xe5\x01\x00\x03E\x97\xd8\nN\xaf%\x8e\xf2\x12^\xd3<\xb6\x01\x00"
        b"\x03E\x97\xd8\x06M\xb2$\x97\x06t\x02\x00\x03E\x97\xd8\x05F\xb2\x1e"
        b"\x7f\xed\x02\x00\x03F\x8e\xda\x0cQ\xc3,\x8f\xfa\x1aj\xdfK\xb2\x13\x85"
        b"\x02\x00\x03E\x97\xd8\rY\xc8:\xac\r{\x9b\xe7\\\xbf \x93\xb3\x02\x00"
        b"\x03E\x97\xd8\x08M\xc3(\x9a\x0e\x82\xf1_\x02\x00\x03X\xaa\xff\x0fVv"
        b"\xda?_\xa0\x12\x84\xe5X\xbb\x1c\x81\xf5V\x02\x00\x03E\x97\xd8\x0eP"
        b"\xc27\xa5\x144|\xe1O\xc1*\x9b\x10u\x03\x00\x03E\x97\xd8\x0bW\xcc5"
        b"\xaf\xcf\x10\x82\xe3\xddG\xb6\x03\x00\x03E\x97\xd8\x05U\xba\x1e\x90"
        b"\xff\x03\x00\x03E\x97\xd8\x0fV\xb7\x19\x8b\xf4Y\xc5\xe5'\x88\xfa"
        b"\\\xcb>\x9f\x03\x00\x03E\x97\xd8\x11^\xbf3\x9b\x00u\xe8\x08O\xbe,"
        b"\x13t\xe0V\xbb.\x03\x00\x03E\x97\xd8\tL\xad\x1f\x8b\xf4b\xca9\xac"
        b"\x03\x00\x0bQ\xba&\x8f\xffd\x84\xd0E2\xa5"
    )
