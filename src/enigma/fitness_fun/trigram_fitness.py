from warnings import warn

from .fitness_fun import FitnessFunction


class TrigramFitness(FitnessFunction):
    @staticmethod
    def __tri_index(self, c1: int, c2: int, c3: int) -> int:
        return (c1 << 10) | (c2 << 5) | c3

    def __init__(self):
        super().__init__()
        self.__trigrams: dict[float] = {}
        try:
            with open("./resources/trigrams.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    key, score = line.split(",")
                    i: int = TrigramFitness.__tri_index(
                        ord(key[0])-65, ord(key[1])-65, ord(key[2])-65
                    )
                    self.__trigrams[chr(i)] = float(score)
        except FileNotFoundError:
            warn("Trigrams configuration file not found")

    def score(self, text: str) -> float:
        fitness: float = 0.0
        current: int = 0
        next1: int = ord(text[0]) - 65
        next2: int = ord(text[1]) - 65
        for c in text[2:]:
            current = next1
            next1 = next2
            next1 = ord(c) - 65
            fitness += self.__trigrams[self.__tri_index(current, next1, next2)]
        return fitness
