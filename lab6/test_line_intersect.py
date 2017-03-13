from line_intersect import line_intersect
import unittest


class TestLineIntersect(unittest.TestCase):
    """
    Test for line_intersect function.
    """
    def setUp(self):
        self.line1 = [(0.0, 0.0), (2.0, 4.0)]
        self.line2 = [(0.0, 2.0), (1.0, 0.0)]
        self.line3 = [(1.0, 2.0), (3.0, 6.0)]
        self.line4 = [(2.0, 6.0), (3.0, 4.0)]
        self.line5 = [(0.0, 2.0), (2.0, 2.0)]

    def test_unintersected_lines1(self):
        assert line_intersect(self.line2, self.line3) == None

    def test_unintersected_lines2(self):
        assert line_intersect(self.line1, self.line4) == None

    def test_intersected_lines1(self):
        assert line_intersect(self.line1, self.line2) == (0.5, 1.0)

    def test_intersected_lines2(self):
        assert line_intersect(self.line3, self.line4) == (2.5, 5.0)

    def test_intersected_lines3(self):
        assert line_intersect(self.line1, self.line5) == (1.0, 2.0)

    def test_imposed(self):
        assert line_intersect(self.line1, self.line3) == self.line1
