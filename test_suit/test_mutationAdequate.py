import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):
    
    # Below 3 cases cover the first decision case of invalid side values
    def test_invalid_side_a(self):
        actual = Triangle.classify(-5, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_invalid_side_b(self):
        actual = Triangle.classify(10, -5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_invalid_side_c(self):
        actual = Triangle.classify(10, 10, -5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # Covers Equilateral triangle case
    def test_valid_sides(self):
        actual = Triangle.classify(10,10,10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    # Covers if a!=b
    def test_a_neq_b(self):
        actual = Triangle.classify(2,3,4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    # Covers if a!=c
    def test_a_neq_c(self):
        actual = Triangle.classify(2,3,4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    # Covers if b!=c
    def test_b_neq_c(self):
        actual = Triangle.classify(2,3,4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    """
    Below 3 test cases include the decision cases for isosceles triangle and the individual side comparisons
    """
    # Covers if a==c
    def test_a_eq_c(self):
        actual = Triangle.classify(2,1,2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    # Covers if a==b
    def test_a_eq_b(self):
        actual = Triangle.classify(2,2,1)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    # Covers if b==c
    def test_b_eq_c(self):
        actual = Triangle.classify(1,2,2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    # Covers case for Scalene traingle (redundant)
    def test_if_trans_eq_zero_scalene(self):
        actual = Triangle.classify(2,3,4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
        
    # Covers case for a non valid triangle with trian==0
    def test_if_trian_eq_zero_invalid(self):
        actual = Triangle.classify(2,4,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()