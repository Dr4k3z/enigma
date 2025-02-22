from enum import Enum
from sys import float_info

from fitness_fun import FitnessFunction

from .enigma import Enigma
from .key import EnigmaKey, ScoredEnigmaKey
from .plugboard import Plugboard


class AvailableRotors(Enum):
    Three = 1
    Five = 2
    Eight = 3


class Analysis:
    @staticmethod
    def find_rotor_config(
            cipher: str, rotors: AvailableRotors,
            plugboard: Plugboard, fitness: FitnessFunction) -> ScoredEnigmaKey:

        rotors_list: list[str] = []
        match rotors:
            case AvailableRotors.Three:
                rotors_list = ["I", "II", "III"]
            case AvailableRotors.Five:
                rotors_list = ["I", "II", "III", "IV", "V"]
            case AvailableRotors.Eight:
                rotors_list = [
                    "I", "II", "III", "IV", "V", "VI", "VII", "VIII"
                ]
            case _:
                raise ValueError("Invalid rotor count")

        optimal_rotors: list[str] = []
        optimal_pos: list[int] = []
        key_set: list[ScoredEnigmaKey] = []

        for r1 in rotors_list:
            for r2 in rotors_list:
                if r1 == r2:
                    continue
                for r3 in rotors_list:
                    if r3 == r1 or r3 == r2:
                        continue
                    print(f'{r1} - {r2} - {r3}')

                    max_fitness: float = -float_info.max
                    best_key: EnigmaKey = EnigmaKey()

                    for p1 in range(26):
                        for p2 in range(26):
                            for p3 in range(26):
                                machine: Enigma = Enigma(
                                    rotors=[r1, r2, r3],
                                    reflector="B",
                                    rotor_pos=[p1, p2, p3],
                                    ring_set=[0, 0, 0],
                                    connections=plugboard.connections
                                )

                                decrypted: str = machine.encrypt(cipher)
                                score: float = fitness.score(decrypted)
                                if score > max_fitness:
                                    max_fitness = score

                                    optimal_rotors = [
                                        machine.left_rotor.name,
                                        machine.middle_rotor.name,
                                        machine.right_rotor.name
                                    ]

                                    optimal_pos = [p1, p2, p3]

                                    best_key = EnigmaKey(
                                        rotors=optimal_rotors,
                                        indicators=optimal_pos,
                                        connections=plugboard.connections
                                    )
                key_set.append(ScoredEnigmaKey(best_key, max_fitness))

        key_set.sort(reverse=True)
        return key_set[0]
