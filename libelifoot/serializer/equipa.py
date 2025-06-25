from typing import Any

from libelifoot.entity.equipa import Equipa
from libelifoot.serializer.base_serializer import BaseSerializer
from libelifoot.serializer.coach import CoachSerializer
from libelifoot.serializer.player import PlayerSerializer
from libelifoot.util.crypto import encrypt


class EquipaSerializer(BaseSerializer):

    @staticmethod
    def serialize(obj: Any) -> bytearray | None:
        if not isinstance(obj, Equipa):
            return None

        equipa = bytearray(b'EFa' + b'\x00' * 47)

        equipa += encrypt(obj.ext_name)
        equipa += encrypt(obj.short_name)
        equipa += bytearray(obj.colors.background + b'\x00')
        equipa += bytearray(obj.colors.text + b'\x00')
        equipa += encrypt(obj.country)
        equipa += bytearray(obj.level.to_bytes())
        equipa += bytearray(len(obj.players).to_bytes())
        for p in obj.players:
            equipa += PlayerSerializer.serialize(p)

        equipa += CoachSerializer.serialize(obj.coach)

        return equipa
