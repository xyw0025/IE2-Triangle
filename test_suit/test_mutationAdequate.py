import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):
    
    # To detect mutation - changes the valid condition of input
    def test_valid_values_entire_condition(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    # We are doing the same case with different values to detect any value mutation 
    # That is if say mutation is a<=b or a<=c, then we should detect that mutation
    # Below 3 cases also detect most of the changes that are made in the decision checks for a scalene traingle
    def test_valid_values_ind_cond__a(self):
        actual = Triangle.classify(12, 5, 8)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    def test_valid_values_ind_cond_b(self):
        actual = Triangle.classify(5, 12, 8)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    def test_valid_values_ind_cond_c(self):
        actual = Triangle.classify(5, 8, 12)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    # Additional test cases to detect mutations in the conditions for Scalene triangle
    def test_scalene_cond_a_b(self):
        actual = Triangle.classify(2,3,5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_scalene_cond_a_c(self):
        actual = Triangle.classify(2,5,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_scalene_cond_b_c(self):
        actual = Triangle.classify(5,2,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

               
    # To detect mutation - if not valid inputs but does not return INVALID
    def test_incorrect_return_valid_value_a(self):
        actual = Triangle.classify(-5, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_incorrect_return_valid_value_b(self):
        actual = Triangle.classify(10, -5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_incorrect_return_valid_value_c(self):
        actual = Triangle.classify(10, 10, -5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # Test mutations in the input with one side as zero
    def test_incorrect_value_a(self):
        actual = Triangle.classify(0, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_incorrect_value_b(self):
        actual = Triangle.classify(10, 0, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_incorrect_value_c(self):
        actual = Triangle.classify(10, 10, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    # Tests to detect mutations in the scalene triangle conditions
    # If a+b<=c
    def test_scalene_a_b(self):
        actual = Triangle.classify(5, 7, 14)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_scalene_a_c(self):
        actual = Triangle.classify(5, 14, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_scalene_b_c(self):
        actual = Triangle.classify(14, 5, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


    # Tests for change in the update equations of trian
    def test_initial_val_trian(self):
        actual = Triangle.classify(2, 3, 4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_update_a_b_trian(self):
        actual = Triangle.classify(10, 10, 15)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_update_a_c_trian(self):
        actual = Triangle.classify(10, 15, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_update_b_c_trian(self):
        actual = Triangle.classify(15, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    #Test to detect mutation in the check condition/return of equilateral triangle
    def test_equilateral_cond_check(self):
        actual = Triangle.classify(7, 7, 7)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
    
    #Test to detect mutants in the check conditions/returns for isosceles triangle
    def test_check_a_b_iso(self):
        actual = Triangle.classify(7, 7, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_check_iso_a_b_eq_cond(self):
        actual = Triangle.classify(7, 7, 14)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_check_iso_a_b_geq_cond(self):
        actual = Triangle.classify(7, 7, 15)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_check_a_c_iso(self):
        actual = Triangle.classify(7, 10, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_check_iso_a_c_eq_cond(self):
        actual = Triangle.classify(7, 14, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_check_iso_a_c_geq_cond(self):
        actual = Triangle.classify(7, 15, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_check_b_c_iso(self):
        actual = Triangle.classify(10, 7, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_check_iso_b_c_eq_cond(self):
        actual = Triangle.classify(14, 7, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_check_iso_b_c_geq_cond(self):
        actual = Triangle.classify(15, 7, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
if __name__ == '__main__':
    unittest.main()