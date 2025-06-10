from libelifoot.serializer.base_serializer import BaseSerializer
from libelifoot.util.crypto import encrypt


class CoachSerializer(BaseSerializer):

    @staticmethod
    def serialize(obj: str) -> bytearray:
        coach = bytearray()

        coach.append(0)
        coach += encrypt(obj)

        return coach
