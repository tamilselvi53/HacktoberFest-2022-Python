import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Decimal To Binary Test Cases"""
    def decimal_to_binary_test_a(self):
        """Test Case A"""
        self.assertEqual(solution(2), 10 , "Normal Test 1 Failed")
    
    def decimal_to_binary_test_b(self):
        """Test Case B"""
        self.assertEqual(solution(30), 11110 , "Normal Test 2 Failed")

    def decimal_to_binary_test_c(self):
        """Test Case C"""
        self.assertEqual(solution(40000000), 1001011001100000000000000000000 , "Normal Test 3 Failed")

    def decimal_to_binary_test_d(self):
        """Test Case D"""
        self.assertEqual(solution(500000000000000000000000000000000), 111010110111100110100010101000000000000000000000000000000000000 , "Normal Test 4 Failed")

    def decimal_to_binary_test_e(self):
        """Exception Test Case"""
        self.assertEqual(solution(0), 0 , "Exception Test 1 Failed")

    def decimal_to_binary_test_f(self):
        """Exception Test Case"""
        self.assertEqual(solution(-1), 0 , "Exception Test 2 Failed")

    def decimal_to_binary_test_g(self):
        """Exception Test Case"""
        self.assertEqual(solution(1.5), 0 , "Exception Test 3 Failed")

    def decimal_to_binary_test_h(self):
        """Exception Test Case"""
        self.assertEqual(solution(1.0), 0 , "Exception Test 4 Failed")

    def decimal_to_binary_test_i(self):
        """Exception Test Case"""
        self.assertEqual(solution(), 0 , "Exception Test 5 Failed")

if __name__ == "__main__":
    unittest.main()