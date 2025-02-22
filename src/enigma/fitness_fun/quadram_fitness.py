from warnings import warn

from .fitness_fun import FitnessFunction


class QuadramFitness(FitnessFunction):
    @staticmethod
    def __quad_index(c1: int, c2: int, c3: int, c4: int) -> int:
        return (c1 << 15) | (c2 << 10) | (c3 << 5) | c4

    def __init__(self) -> None:
        super().__init__()
        try:
            with open("src/enigma/fitness_fun/quadram.txt") as f:
                self.__quadrams = {
                    line.split()[0]: float(line.split()[1]) for line in f
                }
        except FileNotFoundError:
            warn('File not found')
            self.__quadrams = {}

    def score(self, text: str) -> float:
        fitness: float = 0.0

        for i in range(len(text) - 3):
            quad = self.__quad_index(
                ord(text[i]) - 65, ord(text[i + 1]) - 65, ord(text[i + 2]) - 65, ord(text[i + 3]) - 65 # noqa
            )
            fitness += self.__quadrams.get(quad, self.eps)

        return fitness
