import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):
    def test_equilateral(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
    
    def test_scalene(self):
        actual = Triangle.classify(2,3,4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_isosceles_a_b(self):
        actual = Triangle.classify(2,2,3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_isosceles_a_c(self):
        actual = Triangle.classify(2,3,2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_isosceles_b_c(self):
        actual = Triangle.classify(3,2,2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_invalid_side_a(self):
        actual = Triangle.classify(-5,10,10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_invalid_side_b(self):
        actual = Triangle.classify(10,-5,10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_invalid_side_c(self):
        actual = Triangle.classify(10,10,-5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_violate_inequality_a_b(self):
        actual = Triangle.classify(10,5,17)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_violate_inequality_a_c(self):
        actual = Triangle.classify(10,17,5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_violate_inequality_b_c(self):
        actual = Triangle.classify(17,10,5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()