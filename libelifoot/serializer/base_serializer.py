from abc import abstractmethod, ABC
from typing import Any


class BaseSerializer(ABC):

    @staticmethod
    @abstractmethod
    def serialize(obj: Any) -> bytearray | None:
        pass # pragma: no cover
