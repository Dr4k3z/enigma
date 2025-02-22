from collections import Counter

from .fitness_fun import FitnessFunction


class IOC(FitnessFunction):
    def __init__(self) -> None:
        super().__init__()

    def score(self, text: str) -> float:
        histogram: Counter[str] = Counter(text)
        n: int = len(text)
        total: float = 0.0

        for _, freq in histogram.items():
            total += freq * (freq - 1)

        return total / (n * (n - 1))
