from is_sorted import is_sorted
import unittest


class TestIsSorted(unittest.TestCase):
    def test_list_with_float(self):
        arg = [1, 2.1, 3]
        expected = False
        assert is_sorted(arg) == expected

    def test_empty_list(self):
        arg = []
        expected = True
        assert is_sorted(arg) == expected

    def test_list_with_one_element(self):
        arg = [1]
        expected = True
        assert is_sorted(arg) == expected

    def test_sorted_list(self):
        arg = [1, 2, 3]
        expected = True
        assert is_sorted(arg) == expected

    def test_unsorted_list(self):
        arg = [1, 3, 2]
        expected = False
        assert is_sorted(arg) == expected

    def test_list_with_same_element(self):
        arg = [1, 2, 2, 3, 3]
        expected = True
        assert is_sorted(arg) == expected

if __name__ == '__main__':
    unittest.main()
