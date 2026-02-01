from abc import ABC, abstractmethod
from typing import Any


class BaseCmd(ABC): # pragma: no cover

    @abstractmethod
    def run(self) -> Any:
        pass
