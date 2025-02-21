"""
Enigma implementation
"""

from .plugboard import Plugboard
from .reflector import Reflector
from .rotor import Rotor


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

    # copy constructor?

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


class Enigma:
    def __init__(
        self,
        rotors: list[str],
        reflector: str,
        rotor_pos: list[int],
        ring_set: list[int],
        connections: str,
    ) -> None:

        self.left_rotor: Rotor = Rotor.create_rotor(
            rotors[0], rotor_pos[0], ring_set[0]
        )
        self.middle_rotor: Rotor = Rotor.create_rotor(
            rotors[1], rotor_pos[1], ring_set[1]
        )
        self.right_rotor: Rotor = Rotor.create_rotor(
            rotors[2], rotor_pos[2], ring_set[2]
        )

        self.reflector: Reflector = Reflector.create_reflector(reflector)

        self.plugboard: Plugboard = Plugboard(connections)

    @classmethod
    def create_enigma(cls, key: EnigmaKey) -> "Enigma":
        return cls(key.rotors, "B", key.indicators, key.rings, key.connections)

    def rotate(self) -> None:
        if self.middle_rotor.is_at_notch():
            self.middle_rotor.turnover()
            self.left_rotor.turnover()
        elif self.right_rotor.is_at_notch():
            self.middle_rotor.turnover()

        self.right_rotor.turnover()

    def __encrypt_int(self, c: int) -> int:
        self.rotate()

        # plugboard - in
        c = self.plugboard.forward(c)

        # rotors - right to left
        c = self.right_rotor.forward(c)
        c = self.middle_rotor.forward(c)
        c = self.left_rotor.forward(c)

        # reflector
        c = self.reflector.forward(c)

        # rotors - left to right
        c = self.left_rotor.backward(c)
        c = self.middle_rotor.backward(c)
        c = self.right_rotor.backward(c)

        # plugboard - out
        c = self.plugboard.forward(c)

        # print(f"Debug: {c}")
        return c

    def __enctrypt_char(self, c: str) -> str:
        if len(c) > 1:
            raise ValueError("You must pass only one char")

        # print(f'encrypting {c}')

        if "A" <= c <= "Z":
            return chr((self.__encrypt_int(ord(c) - ord("A")) + ord("A")))
        elif "a" <= c <= "z":
            return chr((self.__encrypt_int(ord(c) - ord("a")) + ord("a")))
        else:
            raise ValueError("Character is not a letter")

    def __encrypt_str(self, s: str) -> str:
        return "".join(self.__enctrypt_char(c) for c in s)

    def encrypt(self, value: int | str) -> int | str:
        if isinstance(value, int):
            return self.__encrypt_int(value)
        elif isinstance(value, str):
            if len(value) == 1:
                return self.__enctrypt_char(value)
            else:
                return self.__encrypt_str(value)
        else:
            raise TypeError("Unsupported type for encryption")