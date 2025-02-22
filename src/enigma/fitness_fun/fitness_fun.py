from abc import ABC, abstractmethod


class FitnessFunction(ABC):
    def __init__(self) -> None:
        self.eps: float = 3e-6

    @abstractmethod
    def score(self, text: str) -> float:
        return 0.0
