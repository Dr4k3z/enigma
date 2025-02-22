class EnigmaKey:
    def __init__(
        self,
        rotors: list[str] = ["I", "II", "III"],
        indicators: list[int] = [0, 0, 0],
        rings: list[int] = [0, 0, 0],
        connections: str = "",
    ) -> None:

        self.__rotors: list[str] = rotors
        self.__indicators: list[int] = indicators
        self.__rings: list[int] = rings
        self.__connections: str = connections

    @property
    def rotors(self):
        return self.__rotors

    @property
    def indicators(self):
        return self.__indicators

    @property
    def rings(self):
        return self.__rings

    @property
    def connections(self):
        return self.__connections


class ScoredEnigmaKey(EnigmaKey):
    def __init__(self, key: EnigmaKey, score: float) -> None:
        super().__init__(
            key.rotors,
            key.indicators,
            key.rings,
            key.connections
        )
        self.__score: float = score

    @property
    def score(self):
        return self.__score

    def __lt__(self, other: 'ScoredEnigmaKey') -> bool:
        return self.__score < other.score
