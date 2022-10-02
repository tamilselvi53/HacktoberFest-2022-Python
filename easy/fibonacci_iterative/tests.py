import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Fibonacci Test Cases"""

    def test_fibonacci_a(self):
        """Normal Test 1"""
        self.assertEqual(solution(3),2, "Normal Test 1 Failed")

    def test_fibonacci_b(self):
        """Normal Test 2"""
        self.assertEqual(solution(5),5, "Normal Test 2 Failed")

    def test_fibonacci_c(self):
        """Normal Test 3"""
        self.assertEqual(solution(9),34, "Normal Test 3 Failed")

    def test_fibonacci_d(self):
        """Normal Test 4"""
        self.assertEqual(solution(27),196418, "Normal Test 4 Failed")

    def test_fibonacci_e(self):
        """Exception Test 1"""
        self.assertEqual(solution(1),1, "Exception Test 1 Failed")

    def test_fibonacci_f(self):
        """Exception Test 2"""
        self.assertEqual(solution(0),0, "Exception Test 2 Failed")

    def test_fibonacci_g(self):
        """Exception Test 3"""
        self.assertEqual(solution(-1),-1, "Exception Test 3 Failed")

    def test_fibonacci_h(self):
        """Exception Test 4"""
        self.assertEqual(solution(),-1, "Exception Test 4 Failed")

if __name__ == '__main__':
    utility.main()