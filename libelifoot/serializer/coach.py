from typing import Any, Optional

from libelifoot.serializer.base_serializer import BaseSerializer
from libelifoot.util.crypto import encrypt


class CoachSerializer(BaseSerializer):

    @staticmethod
    def serialize(obj: Any) -> Optional[bytearray]:
        if not isinstance(obj, str):
            return None

        coach = bytearray(b'\x00')
        coach += encrypt(obj)

        return coach
