from libelifoot.entity.player import Player
from libelifoot.serializer.player import PlayerSerializer
from libelifoot.util.player_position import PlayerPosition


def test_serialize_none_player():
    ret = PlayerSerializer.serialize(None)

    assert ret is None


def test_serialize_valid_player():
    player = Player(name='Ronaldo', position=PlayerPosition.A.name,
                    country='BRA')
    expected = bytearray(b'\x00\x03E\x97\xd8\x07Y\xc86\x97\x03g\xd6\x03')

    ret = PlayerSerializer.serialize(player)

    assert ret == expected
