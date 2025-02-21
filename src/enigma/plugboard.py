"""
    Plugboard implementation
"""
import re


class Plugboard:
    def __init__(self, connections: str) -> None:
        self.__wiring: list[int] = self.decode_plugboard(connections)

    def forward(self, c: int) -> int:
        return self.__wiring[c]

    @staticmethod
    def identity_plugboard() -> list[int]:
        return [i for i in range(26)]

    @staticmethod
    def unplugged_chars(connections: str) -> set[int]:
        unplugged: set = set([i for i in range(26)])

        if connections == '':
            return unplugged

        pairs: list[str] = re.split(r'[^a-zA-Z]', connections)

        for p in pairs:
            c1: int = ord(p[0]) - 65
            c2: int = ord(p[1]) - 65
            unplugged.remove(c1)
            unplugged.remove(c2)

        return unplugged

    @classmethod
    def decode_plugboard(cls, connections: str) -> list[int]:
        if connections == '':
            return cls.identity_plugboard()

        pairs: list[str] = re.split(r'[^a-zA-Z]', connections)
        plugged: set = set()
        mapping: list[int] = cls.identity_plugboard()

        for p in pairs:
            if len(p) != 2:
                return cls.identity_plugboard()

            c1: int = ord(p[0]) - 65
            c2: int = ord(p[1]) - 65

            if c1 in plugged or c2 in plugged:
                return cls.identity_plugboard()

            plugged.add(c1)
            plugged.add(c2)

            mapping[c1] = c2
            mapping[c2] = c1

        return mapping
