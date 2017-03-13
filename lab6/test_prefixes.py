from all_prefixes import all_prefixes
import unittest


class TestAllPrefixes(unittest.TestCase):
    def test_word_with_one_letter(self):
        arg = "a"
        expected = {"a"}
        assert all_prefixes(arg) == expected

    def test_word_with_one_first_letter(self):
        arg = "lead"
        expected = {"l", "le", "lea", "lead"}
        assert all_prefixes(arg) == expected

    def test_word_with_few_first_letters(self):
        arg = "avangard"
        expected = {"a", "av", "ava", "avan", "avang", "avanga", "avangar",
                    "avangard", "an", "ang", "anga", "angar", "angard", "ar", "ard"}
        assert all_prefixes(arg) == expected

    def test_word_with_first_letter_at_the_end(self):
        arg = "rar"
        expected = {"r", "ra", "rar"}
        assert all_prefixes(arg) == expected

if __name__ == '__main__':
    unittest.main()
