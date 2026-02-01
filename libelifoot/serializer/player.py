from typing import Any, Optional

from libelifoot.entity.player import Player
from libelifoot.serializer.base_serializer import BaseSerializer
from libelifoot.util.player_position import PlayerPosition
from libelifoot.util.crypto import encrypt


class PlayerSerializer(BaseSerializer):

    @staticmethod
    def serialize(obj: Any) -> Optional[bytearray]:
        if not isinstance(obj, Player):
            return None

        player = bytearray(b'\x00')
        player += encrypt(obj.country)
        player += encrypt(obj.name)
        player.append(PlayerPosition.to_pos_code(obj.position))

        return player
