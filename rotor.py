"""
    Rotor implementation
"""


enconding_dict: dict = {
            'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
            'IV': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
            'V': 'VZBRGITYUPSDNHLXAWMJQOFECK',
            'VI': 'JPGVOUMFYQBENHZRDKASXLICTW',
            'VII': 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
            'VIII': 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
            'default': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        }


notch_dict: dict = {
            'I': 16,
            'II': 4,
            'III': 21,
            'IV': 9,
            'V': 25,
            'VI': 0,
            'VII': 0,
            'VIII': 0,
            'default': 0
        }


class Rotor:
    def __init__(self, name: str, enconding: str, rotor_pos: int, notch_pos: int, ring_set: int) -> None:
        self.__name: str = name
        self.enconding: str = enconding
        self.__rotor_pos: int = rotor_pos
        self.__notch_pos: int = notch_pos
        self.__ring_set: int = ring_set

        self.__fwd_wiring: list[int] = self.decode_wiring(enconding)
        self.__backwd_wiring: list[int] = self.inverse_wiring(self.__fwd_wiring)

    @classmethod
    def create_rotor(cls, name: str, rotor_pos: int, ring_set: int) -> 'Rotor':
        match name:
            case name if name in ['I', 'II', 'III', 'IV', 'V']:
                return cls(name, enconding_dict[name], rotor_pos, notch_dict[name], ring_set)
            case 'VI':
                raise NotImplementedError(f'Rotor name {name} has not been implemented yet')
            case 'VII':
                raise NotImplementedError(f'Rotor name {name} has not been implemented yet')
            case 'VIII':
                raise NotImplementedError(f'Rotor name {name} has not been implemented yet')
            case _:
                return cls('Identity', enconding_dict['default'], rotor_pos, notch_dict['default'], ring_set)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def rotor_pos(self) -> int:
        return self.__rotor_pos

    @staticmethod
    def decode_wiring(enconding: str) -> list[int]:
        N: int = len(enconding)
        wiring: list = [None]*N

        for i in range(N):
            wiring[i] = ord(enconding[i]) - 65

        return wiring

    @staticmethod
    def inverse_wiring(wiring: list[int]) -> list[int]:
        N: int = len(wiring)
        inverse: list = [None]*N

        for i in range(N):
            forward: int = wiring[i]
            inverse[forward] = i

        return inverse

    @staticmethod
    def encipher(k: int, pos: int, ring: int, mapping: list[int]) -> int:
        shift: int = pos-ring
        return (mapping[(k + shift + 26) % 26] - shift+26) % 26

    def forward(self, c: int) -> int:
        return self.encipher(c, self.__rotor_pos, self.__ring_set, self.__fwd_wiring)

    def backward(self, c: int) -> int:
        return self.encipher(c, self.__rotor_pos, self.__ring_set, self.__backwd_wiring)

    def is_at_notch(self) -> bool:
        return self.__notch_pos == self.__rotor_pos

    def turnover(self) -> None:
        self.__rotor_pos = (self.__rotor_pos + 1) % 26
