import random

from enigma import Enigma


def test_encrypt():
    # Basic settings
    e = Enigma(["I", "II", "III"], "B", [0, 0, 0], [0, 0, 0], "")
    input_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBABCDEFGHIJKLMNOPQRSTUVWXYZ"
    expected_output = "BJELRQZVJWARXSNBXORSTNCFMEYHCXTGYJFLINHNXSHIUNTHEORXOPLOVFEKAGADSPNPCMHRVZCYECDAZIHVYGPITMSRZKGGHLSRBLHL"
    ciphertext = e.encrypt(input_text)
    assert expected_output == ciphertext

    """
    # Varied rotors
    e = Enigma(["VII", "V", "IV"], "B", [10, 5, 12], [1, 2, 3], "")
    ciphertext = e.encrypt(input_text)
    expected_output = "FOTYBPKLBZQSGZBOPUFYPFUSETWKNQQHVNHLKJZZZKHUBEJLGVUNIOYSDTEZJQHHAOYYZSENTGXNJCHEDFHQUCGCGJBURNSEDZSEPLQP"
    assert expected_output == ciphertext

    # Long input
    e = Enigma(["III", "VI", "VIII"], "B", [3, 5, 9], [11, 13, 19], "")
    long_input = "".join(["A"] * 500)
    ciphertext = e.encrypt(long_input)
    expected_output = (
        "YJKJMFQKPCUOCKTEZQVXYZJWJFROVJMWJVXRCQYFCUVBRELVHRWGPYGCHVLBVJEVTTYVMWKJFOZHLJEXYXRDBEVEHVXKQSBPYZN"
        "IQDCBGTDDWZQWLHIBQNTYPIEBMNINNGMUPPGLSZCBRJULOLNJSOEDLOBXXGEVTKCOTTLDZPHBUFKLWSFSRKOMXKZELBDJNRUDUCO"
        "TNCGLIKVKMHHCYDEKFNOECFBWRIEFQQUFXKKGNTSTVHVITVHDFKIJIHOGMDSQUFMZCGGFZMJUKGDNDSNSJKWKENIRQKSUUHJYMIG"
        "WWNMIESFRCVIBFSOUCLBYEEHMESHSGFDESQZJLTORNFBIFUWIFJTOPVMFQCFCFPYZOJFQRFQZTTTOECTDOOYTGVKEWPSZGHCTQRP"
        "GZQOVTTOIEGGHEFDOVSUQLLGNOOWGLCLOWSISUGSVIHWCMSIUUSBWQIGWEWRKQFQQRZHMQJNKQTJFDIJYHDFCWTHXUOOCVRCVYOHL"
    )
    assert expected_output == ciphertext
    """


def test_decrypt():
    random.seed(42)  # For reproducible tests
    # all_rotors = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

    all_rotors = ["I", "II", "III", "IV", "V"]

    # Generate random input
    input_text = "".join([chr(random.randint(65, 90)) for _ in range(1000)])

    # Run 10 tests with random configurations
    for _ in range(10):
        # Random initialization
        rotors = [random.choice(all_rotors) for _ in range(3)]
        starting_positions = [random.randint(0, 25) for _ in range(3)]
        ring_settings = [random.randint(0, 25) for _ in range(3)]

        # Machine 1 - Encryption
        e1 = Enigma(rotors, "B", starting_positions, ring_settings, "")
        ciphertext = e1.encrypt(input_text)

        # Machine 2 - Decryption
        e2 = Enigma(rotors, "B", starting_positions, ring_settings, "")
        plaintext = e2.encrypt(ciphertext)

        assert input_text == plaintext


def test_plugboard():
    # Simple test - 4 plugs
    e = Enigma(["I", "II", "III"], "B", [0, 0, 0], [0, 0, 0], "AC FG JY LW")
    input_text = "".join(["A"] * 50)
    expected_output = "QREBNMCYZELKQOJCGJVIVGLYEMUPCURPVPUMDIWXPPWROOQEGI"
    output = e.encrypt(input_text)
    assert expected_output == output

    # 6 plugs
    e = Enigma(["IV", "VI", "III"], "B", [0, 10, 6], [0, 0, 0], "BM DH RS KN GZ FQ")
    input_text = "WRBHFRROSFHBCHVBENQFAGNYCGCRSTQYAJNROJAKVKXAHGUZHZVKWUTDGMBMSCYQSKABUGRVMIUOWAPKCMHYCRTSDEYTNJLVWNQY"
    expected_output = "FYTIDQIBHDONUPAUVPNKILDHDJGCWFVMJUFNJSFYZTSPITBURMCJEEAMZAZIJMZAVFCTYTKYORHYDDSXHBLQWPJBMSSWIPSWLENZ"
    output = e.encrypt(input_text)
    assert expected_output == output
    
    # 10 plugs
    e = Enigma(["I", "II", "III"], "B", [0, 1, 20], [5, 5, 4], "AG HR YT KI FL WE NM SD OP QJ")
    input_text = "RNXYAZUYTFNQFMBOLNYNYBUYPMWJUQSBYRHPOIRKQSIKBKEKEAJUNNVGUQDODVFQZHASHMQIHSQXICTSJNAUVZYIHVBBARPJADRH"
    expected_output = "CFBJTPYXROYGGVTGBUTEBURBXNUZGGRALBNXIQHVBFWPLZQSCEZWTAWCKKPRSWOGNYXLCOTQAWDRRKBCADTKZGPWSTNYIJGLVIUQ"
    output = e.encrypt(input_text)
    assert expected_output == output
