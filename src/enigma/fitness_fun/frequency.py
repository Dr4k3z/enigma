from collections import Counter, defaultdict


class FrequencyAnalysis():
    def __init__(self) -> None:
        super().__init__()
        self.__total: int = 0
        self.__counts: defaultdict[str, int] = defaultdict(int)

    def analyse(self, text: str) -> None:
        self.__counts = Counter(text)
        self.__total += len(text)

    def frequencies(self) -> dict[str, float]:
        return {
            char: count / self.__total for char, count in self.__counts.items()
        }
