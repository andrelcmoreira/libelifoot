from abc import abstractmethod, ABC
from typing import Any


class BaseSerializer(ABC): # pragma: no cover

    @staticmethod
    @abstractmethod
    def serialize(obj: Any) -> bytearray | None:
        pass
