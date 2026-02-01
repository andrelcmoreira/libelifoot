from abc import abstractmethod, ABC
from typing import Any, Optional


class BaseSerializer(ABC): # pragma: no cover

    @staticmethod
    @abstractmethod
    def serialize(obj: Any) -> Optional[bytearray]:
        pass
