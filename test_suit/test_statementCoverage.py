import unittest
from isTriangle import Triangle


class TestStatementCoverageTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(-1, -1, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


    def test2(self):
        actual = Triangle.classify(2, 2, 2)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(2, 3, 4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(2, 3, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(2, 2, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(2, 3, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify(3, 2, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test8(self):
        actual = Triangle.classify(5, 2, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
