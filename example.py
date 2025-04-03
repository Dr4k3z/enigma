from enigma import Enigma, EnigmaKey


def encrtpy():
    key = EnigmaKey()
    machine = Enigma.create_enigma(key)
    machine2 = Enigma.create_enigma(key)

    plain = "helloworld"
    res = machine.encrypt(plain)
    res_decrypted = machine2.encrypt(res)

    print(f"Encrypted: {res}")
    print(f"Plain: {res_decrypted}")


if __name__ == "__main__":
    encrtpy()
