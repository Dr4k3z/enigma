from src.enigma import Enigma, EnigmaKey
from src.enigma.fitness_fun import BigramFitness


def encrtpy():
    key = EnigmaKey()
    machine = Enigma.create_enigma(key)
    machine2 = Enigma.create_enigma(key)

    plain = "helloworld"
    res = machine.encrypt(plain)
    res_decrypted = machine2.encrypt(res)

    print(f"Encrypted: {res}")
    print(f"Plain: {res_decrypted}")


def analysis():
    bf = BigramFitness()
    print(bf)


if __name__ == "__main__":
    analysis()