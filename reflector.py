"""
    Reflector implemenation
"""


encoding_dict = {
            'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
            'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
            'default': 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        }


class Reflector:
    def __init__(self, encoding: str) -> None:
        self.__fwd_wiring: list[int] = self.decode_wiring(encoding)

    @classmethod
    def create_reflector(cls, name: str) -> 'Reflector':
        return cls(encoding_dict[name])

    @staticmethod
    def decode_wiring(encoding: str) -> list[int]:
        N = len(encoding)
        wiring: list[int] = [0]*N

        for i in range(N):
            wiring[i] = ord(encoding[i]) - 65

        return wiring

    def forward(self, c: int) -> int:
        return self.__fwd_wiring[c]
