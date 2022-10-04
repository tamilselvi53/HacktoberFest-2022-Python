import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Half Diamond Test Cases"""

    def test_half_diamond_a(self):
        """Normal Test 1"""
        self.assertEqual(solution(5), "1\n12\n123\n1234\n12345", "Normal Test 1 Failed")

    def test_half_diamond_b(self):
        """Normal Test 2"""
        self.assertEqual(solution(3), "1\n12\n123", "Normal Test 2 Failed")

    def test_half_diamond_c(self):
        """Normal Test 3"""
        self.assertEqual(solution(7), "1\n12\n123\n1234\n12345\n123456\n1234567", "Normal Test 3 Failed")

    def test_half_diamond_d(self):
        """Normal Test 4"""
        self.assertEqual(solution(9), "1\n12\n123\n1234\n12345\n123456\n1234567\n12345678\n123456789", "Normal Test 4 Failed")

    def test_half_diamond_e(self):
        """Exception Test 1"""
        self.assertEqual(solution(0), -1, "Exception Test 1 Failed")

    def test_half_diamond_f(self):
        """Exception Test 2"""
        self.assertEqual(solution(-1), -1, "Exception Test 2 Failed")

    def test_half_diamond_g(self):
        """Exception Test 3"""
        self.assertEqual(solution(), -1, "Exception Test 3 Failed")

if __name__ == '__main__':
    utility.main()
