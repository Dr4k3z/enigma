from warnings import warn

from .fitness_fun import FitnessFunction


class SingleCharFitness(FitnessFunction):
    def __init__(self) -> None:
        super().__init__()
        try:
            with open("src/enigma/fitness_fun/single.txt") as f:
                self.__singles = {
                    line.split()[0]: float(line.split()[1]) for line in f
                }
        except FileNotFoundError:
            warn("File not found")
            self.freq = {}

    def score(self, text: str) -> float:
        fitness: float = 0.0

        for c in text:
            fitness += self.__singles[ord(c)-65]
