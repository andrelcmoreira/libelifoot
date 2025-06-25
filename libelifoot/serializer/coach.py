from typing import Any

from libelifoot.serializer.base_serializer import BaseSerializer
from libelifoot.util.crypto import encrypt


class CoachSerializer(BaseSerializer):

    @staticmethod
    def serialize(obj: Any) -> bytearray | None:
        if not isinstance(obj, str):
            return None

        coach = bytearray()

        coach.append(0)
        coach += encrypt(obj)

        return coach
