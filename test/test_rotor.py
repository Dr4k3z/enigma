import pytest
from src.rotor import Rotor


def test_rotor_creation():
    # Test basic rotor creation
    rotor = Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0, 16, 0)
    assert rotor.name == "I"
    assert len(rotor.fwd_wiring) == 26
    assert len(rotor.backwd_wiring) == 26
    assert rotor.rotor_pos == 0
    assert rotor.notch_pos == 16
    assert rotor.ring_set == 0


def test_factory_creation():
    # Test the create_rotor factory method for implemented rotors
    for rotor_name in ["I", "II", "III", "IV", "V"]:
        rotor = Rotor.create_rotor(rotor_name, 0, 0)
        assert rotor.name == rotor_name
        assert len(rotor.fwd_wiring) == 26
        assert len(rotor.backwd_wiring) == 26


def test_unimplemented_rotors():
    # Test that unimplemented rotors raise NotImplementedError
    for rotor_name in ["VI", "VII", "VIII"]:
        with pytest.raises(NotImplementedError):
            Rotor.create_rotor(rotor_name, 0, 0)


def test_default_rotor():
    # Test creation of default "Identity" rotor
    rotor = Rotor.create_rotor("unknown", 0, 0)
    assert rotor.name == "Identity"
    assert rotor.enconding == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_forward():
    rotor = Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 16, 16, 0)
    answer = [7, 4, 2, 25, 10, 18, 11, 1]
    for c in range(8):
        res = rotor.forward(c)
        assert res == answer[c]


def test_backward():
    rotor = Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 16, 16, 0)
    assert rotor.backward(10) == 4


def test_decode_wiring():
    # Test the wiring decoding
    encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wiring = Rotor.decode_wiring(encoding)
    assert len(wiring) == 26
    for i, x in enumerate(wiring):
        assert x == i


def test_inverse_wiring():
    # Test the inverse wiring calculation
    forward = list(range(26))  # [0,1,2,...,25]
    inverse = Rotor.inverse_wiring(forward)
    assert forward == inverse  # Identity mapping should be its own inverse


def test_encipher():
    # Test the encipher method with known values
    mapping = Rotor.decode_wiring("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
    print(mapping)
    # Test with different positions and ring settings
    test_cases = [
        (0, 0, 0, 4),  # Input 'A' with no offsets should map to 'E'
        (0, 1, 0, 9),  # Input 'A' with position 1
        (0, 0, 1, 10),  # Input 'A' with ring setting 1
    ]

    """
        the last test_case could be (0,0,1,19)
        i still need to figure this out
    """

    for input_char, pos, ring, expected in test_cases:
        result = Rotor.encipher(input_char, pos, ring, mapping)
        assert result == expected


def test_forward_backward_consistency():
    # Test that forward followed by backward returns original value
    rotor = Rotor.create_rotor("I", 0, 0)
    for i in range(26):
        forward = rotor.forward(i)
        backward = rotor.backward(forward)
        assert backward == i


def test_turnover():
    # Test rotor turnover
    rotor = Rotor.create_rotor("I", 15, 0)  # Position before notch
    assert not rotor.is_at_notch()
    rotor.turnover()
    assert rotor.rotor_pos == 16
    assert rotor.is_at_notch()
    rotor.turnover()
    assert rotor.rotor_pos == 17
    assert not rotor.is_at_notch()


def test_ring_setting_effect():
    # Test that different ring settings produce different encodings
    rotor1 = Rotor.create_rotor("I", 0, 0)
    result1 = rotor1.forward(0)  # 'A' with ring setting 0

    rotor2 = Rotor.create_rotor("I", 0, 1)
    result2 = rotor2.forward(0)  # 'A' with ring setting 1

    assert (
        result1 != result2
    )  # Different ring settings should produce different results


def test_full_rotation():
    # Test complete rotation through all positions
    rotor = Rotor.create_rotor("I", 0, 0)
    initial_position = rotor.rotor_pos

    # Rotate 26 times
    for _ in range(26):
        rotor.turnover()

    assert rotor.rotor_pos == initial_position  # Should be back at start


"""
def test_enconding_dict_consistency():
    # Test that all encodings in the dictionary are valid
    for name, encoding in enconding_dict.items():
        assert len(encoding) == 26
        # Check that each encoding contains all letters exactly once
        assert sorted(encoding) == sorted("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def test_notch_dict_consistency():
    # Test that all notch positions are valid
    for name, position in notch_dict.items():
        assert 0 <= position <= 25
"""
