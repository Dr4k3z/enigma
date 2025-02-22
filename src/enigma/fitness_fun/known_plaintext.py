from .fitness_fun import FitnessFunction


class KnownPlaintext(FitnessFunction):
    def __init__(self, plain: str):
        super().__init__()
        self.__plain = plain

    @classmethod
    def make_instance(cls, words: list[str], offsets: int):
        length: int = 0
        for i, w in enumerate(words):
            offset: int = offsets[i]+len(w)
            length = max(length, offset)

        plain: str = " ".join(words)
        return cls(plain[:length])

    def score(self, text: str) -> float:
        length: int = min(len(text), len(self.__plain))
        total: int = 0

        for i in range(length):
            if text[i] == self.__plain[i]:
                total += 1

        return total
