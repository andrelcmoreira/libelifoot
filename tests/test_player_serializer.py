from libelifoot.entity.player import Player
from libelifoot.serializer.player import PlayerSerializer


def test_serialize_none_player():
    ret = PlayerSerializer.serialize(None)

    assert ret is None


def test_serialize_valid_player():
    player = Player(name='John doe', position='G', country='BRA')
    expected = bytearray(b'\x00\x03E\x97\xd8\x08R\xc1)\x97\xb7\x1b\x8a\xef\x00')

    ret = PlayerSerializer.serialize(player)

    assert ret == expected
