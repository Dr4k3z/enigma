from warnings import warn

from .fitness_fun import FitnessFunction


class BigramFitness(FitnessFunction):
    def __init__(self) -> None:
        super().__init__()
        self.__bigrams: dict[float] = {}
        try:
            with open('./resources/bigrams.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    key, score = line.split(',')
                    self.__bigrams[str(key)] = float(score)
        except FileNotFoundError:
            warn('Bigrams configuration file not found')

    def __bi_index(self, c1: int, c2: int) -> int:
        return (c1 << 5) | c2

    def score(self, text: str) -> float:
        fitness: float = 0.0
        current: int = 0
        next: int = ord(text[0]) - 65
        for c in text[1:]:
            current = next
            next = ord(c) - 65
            fitness += self.__bigrams[self.__bi_index(current, next)]
        return fitness
