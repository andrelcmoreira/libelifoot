from abc import ABC, abstractmethod


class AsyncCommand(ABC):

    @abstractmethod
    def run(self) -> None:
        pass # pragma: no cover
