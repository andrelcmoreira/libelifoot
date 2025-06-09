from entity.player import Player
from serializer.base_serializer import BaseSerializer
from util.player_position import PlayerPosition
from util.crypto import encrypt


class PlayerSerializer(BaseSerializer):

    @staticmethod
    def serialize(obj: Player) -> bytearray:
        player = bytearray()

        player.append(0)
        player += encrypt(obj.country)
        player += encrypt(obj.name)
        player.append(PlayerPosition.to_pos_code(obj.position))

        return player
