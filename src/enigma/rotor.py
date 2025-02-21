"""
Rotor implementation
"""

enconding_dict: dict = {
    "I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    "IV": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
    "V": "VZBRGITYUPSDNHLXAWMJQOFECK",
    "VI": "JPGVOUMFYQBENHZRDKASXLICTW",
    "VII": "NZJHGRCXMYSWBOUFAIVLPEKQDT",
    "VIII": "FKQHTLXOCBJSPDZRAMEWNIUYGV",
    "default": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
}


notch_dict: dict = {
    "I": 16,
    "II": 4,
    "III": 21,
    "IV": 9,
    "V": 25,
    "VI": 0,
    "VII": 0,
    "VIII": 0,
    "default": 0,
}


class Rotor:
    def __init__(
        self, name: str, enconding: str, rotor_pos: int, notch_pos: int, ring_set: int
    ) -> None:
        """
        Basic constructor of the class, set up all the required information.
        Rarely used, as Rotor's are usually constructed using the factory
        method below.
        """
        self._name: str = name
        self.enconding: str = enconding
        self._rotor_pos: int = rotor_pos
        self._notch_pos: int = notch_pos
        self._ring_set: int = ring_set

        self._fwd_wiring: list[int] = self.decode_wiring(enconding)
        self._backwd_wiring: list[int] = self.inverse_wiring(self._fwd_wiring)

    @classmethod
    def create_rotor(cls, name: str, rotor_pos: int, ring_set: int) -> "Rotor":
        """
        Factory method to create the Rotor. The cases VI,VII,VIII
        are yet to be implemented. They basically need to override
        one method of the class.
        """
        match name:
            case name if name in ["I", "II", "III", "IV", "V"]:
                return cls(
                    name,
                    enconding_dict[name],
                    rotor_pos,
                    notch_dict[name],
                    ring_set
                )
            case name if name in ["VI", "VII", "VIII"]:
                class RotorExtra(Rotor):
                    def is_at_notch(self) -> bool:
                        return self._rotor_pos == 12 or self._rotor_pos == 25
                return RotorExtra(
                    name,
                    enconding_dict[name],
                    rotor_pos,
                    notch_dict[name],
                    ring_set
                )
            case _:
                return cls(
                    "Identity",
                    enconding_dict["default"],
                    rotor_pos,
                    notch_dict["default"],
                    ring_set,
                )

    # getters
    @property
    def name(self) -> str:
        return self._name

    @property
    def rotor_pos(self) -> int:
        return self._rotor_pos

    @property
    def notch_pos(self) -> int:
        return self._notch_pos

    @property
    def ring_set(self) -> int:
        return self._ring_set

    @property
    def fwd_wiring(self) -> list[int]:
        return self._fwd_wiring

    @property
    def backwd_wiring(self) -> list[int]:
        return self._backwd_wiring

    @staticmethod
    def decode_wiring(enconding: str) -> list[int]:
        """
        The method returns ...
        """
        N: int = len(enconding)
        wiring: list = [None] * N

        for i, c in enumerate(enconding):
            wiring[i] = ord(c) - 65

        return wiring

    @staticmethod
    def inverse_wiring(wiring: list[int]) -> list[int]:
        """
        The method returns ...
        """
        N: int = len(wiring)
        inverse: list = [None] * N

        for i in range(N):
            forward: int = wiring[i]
            inverse[forward] = i

        return inverse

    @staticmethod
    def encipher(k: int, pos: int, ring: int, mapping: list[int]) -> int:
        shift: int = pos - ring
        return (mapping[(k + shift + 26) % 26] - shift + 26) % 26

    def forward(self, c: int) -> int:
        return self.encipher(c, self._rotor_pos, self._ring_set, self._fwd_wiring)

    def backward(self, c: int) -> int:
        return self.encipher(c, self._rotor_pos, self._ring_set, self._backwd_wiring)

    def is_at_notch(self) -> bool:
        return self._notch_pos == self._rotor_pos

    def turnover(self) -> None:
        self._rotor_pos = (self._rotor_pos + 1) % 26
