import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Insertion Sort Test Cases"""

    def test_insertion_sort_a(self):
        """Normal Test 1"""
        self.assertEqual(solution([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "Normal Test 1 Failed")

    def test_insertion_sort_b(self):
        """Normal Test 2"""
        self.assertEqual(solution([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "Normal Test 2 Failed")

    def test_insertion_sort_c(self):
        """Normal Test 3"""
        self.assertEqual(solution([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5], "Normal Test 3 Failed")

    def test_insertion_sort_d(self):
        """Normal Test 4"""
        self.assertEqual(solution([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1], "Normal Test 4 Failed")

    def test_insertion_sort_e(self):
        """Exception Test 1"""
        self.assertEqual(solution([]), [], "Exception Test 1 Failed")
    
    def test_insertion_sort_f(self):
        """Exception Test 2"""
        self.assertEqual(solution(), [], "Exception Test 2 Failed")

if __name__ == '__main__':
    utility.main()