from abc import ABC, abstractmethod


class AsyncCommand(ABC): # pragma: no cover

    @abstractmethod
    def run(self) -> None:
        pass
