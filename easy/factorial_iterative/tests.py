import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Factorial Testcases"""

    def test_factorial_a(self):
        """Normal Test 1"""
        self.assertEqual(solution(3),6, "Normal Test 1 Failed")

    def test_factorial_b(self):
        """Normal Test 2"""
        self.assertEqual(solution(5),120, "Normal Test 2 Failed")

    def test_factorial_c(self):
        """Normal Test 3"""
        self.assertEqual(solution(9),362880, "Normal Test 3 Failed")

    def test_factorial_d(self):
        """Normal Test 4"""
        self.assertEqual(solution(27), 10888869450418352160768000000, "Normal Test 4 Failed")

    def test_factorial_e(self):
        """Exception Test 1"""
        self.assertEqual(solution(1),1, "Exception Test 1 Failed")

    def test_factorial_f(self):
        """Exception Test 2"""
        self.assertEqual(solution(0),1, "Exception Test 2 Failed")

    def test_factorial_g(self):
        """Exception Test 3"""
        self.assertEqual(solution(-1),-1, "Exception Test 3 Failed")

    def test_factorial_h(self):
        """Exception Test 4"""
        self.assertEqual(solution(),-1, "Exception Test 4 Failed")

if __name__ == '__main__':
    unittest.main()