from vigenere_cipher import VigenereCipher
import unittest


class TestVigenereCipher(unittest.TestCase):
    def test_encode(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_character(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        assert encoded == "X"

    def test_encode_spaces(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_lowercase(self):
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_combine_character(self):
        assert VigenereCipher.combine_character("E", "T") == "X"
        assert VigenereCipher.combine_character("N", "R") == "E"

    def test_extend_keyword(self):
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        assert extended == "TRAINTRAINTRAINT"

    def test_extend_keyword_even(self):
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(15)
        assert extended == "TRAINTRAINTRAIN"

    def test_separate_character(self):
        assert VigenereCipher.separate_character("X", "T") == "E"
        assert VigenereCipher.separate_character("E", "R") == "N"

    def test_decode(self):
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        assert decoded == "ENCODEDINPYTHON"

if __name__ == '__main__':
    unittest.main()
