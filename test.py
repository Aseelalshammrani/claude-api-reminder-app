import unittest
import math
from main import calculate_pi


class TestCalculatePi(unittest.TestCase):
    """Test suite for the calculate_pi function"""
    
    def test_pi_to_5_digits(self):
        """Test that pi is calculated correctly to 5 decimal places"""
        result = calculate_pi(5)
        expected = 3.14159
        self.assertEqual(result, expected)
        
    def test_pi_to_2_digits(self):
        """Test pi calculation with 2 decimal places"""
        result = calculate_pi(2)
        expected = 3.14
        self.assertEqual(result, expected)
        
    def test_pi_to_3_digits(self):
        """Test pi calculation with 3 decimal places"""
        result = calculate_pi(3)
        expected = 3.142
        self.assertEqual(result, expected)
    
    def test_pi_to_4_digits(self):
        """Test pi calculation with 4 decimal places"""
        result = calculate_pi(4)
        expected = 3.1416
        self.assertEqual(result, expected)
    
    def test_pi_default_precision(self):
        """Test that default precision is 5 digits"""
        result = calculate_pi()
        expected = 3.14159
        self.assertEqual(result, expected)
        
    def test_pi_accuracy(self):
        """Test that calculated pi is close to math.pi"""
        result = calculate_pi(5)
        # Check that our result is within a very small tolerance of math.pi
        self.assertAlmostEqual(result, math.pi, places=5)
        
    def test_pi_to_1_digit(self):
        """Test pi calculation with 1 decimal place"""
        result = calculate_pi(1)
        expected = 3.1
        self.assertEqual(result, expected)
        
    def test_pi_value_range(self):
        """Test that pi is in the correct range"""
        result = calculate_pi(5)
        self.assertGreater(result, 3.14159)
        self.assertLess(result, 3.14160)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
