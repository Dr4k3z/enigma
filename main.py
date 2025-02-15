from enigma import Enigma, EnigmaKey


if __name__ == "__main__":
    key = EnigmaKey()
    machine: Enigma = Enigma.create_enigma(key)

    msg = machine.encrypt('TIAMOSARCI')
    print(msg)
