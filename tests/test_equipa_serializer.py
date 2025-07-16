from libelifoot.entity.color import Color
from libelifoot.entity.equipa import Equipa
from libelifoot.entity.player import Player
from libelifoot.serializer.equipa import EquipaSerializer
from libelifoot.util.player_position import PlayerPosition


def test_serialize_none_equipa():
    ret = EquipaSerializer.serialize(None)

    assert ret is None


def test_serialize_valid_equipa():
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
    expected = bytearray(
        b"EFa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17]\xcc>"
        b"\xb2\x13\x7f\xe4^\xbf\xdf$\x97\x07v\xe8\\\xc1\xe1$\x90\x05g\xcc\tO"
        b"\xbe0\xa4\x05q\xd6P\xb1\x00\x00\x03E\x97\xd8\n\x04\x00\x03E\x97\xd8"
        b"\x0cV\xc5\xa8\x177\x89\xf2U\xb6(\x8c\xfb\x00\x00\x03D\x96\xdd\x0eS"
        b"\xc0!\x8f\x04i\xd5\xf57\xa9\x96\no\xe9\x01\x00\x03E\x97\xd8\x07T\xb5"
        b"\'\x90\xfef\xd5\x03\x00\x03E\x97\xd8\x0ce\xc6-\x9c\xbc\x0cu\xe0A\xa4"
        b"\x0c\x81\x03\x00\x12\\\xd12\xa0\xc0\x10q\xd3?\xae\xce$\x93\xfds\xe2F"
        b"\xa7")

    ret = EquipaSerializer.serialize(equipa)

    assert ret == expected
