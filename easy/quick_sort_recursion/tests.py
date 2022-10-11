import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Quick Sort Test"""
    def test_bubble_sort_test_a(self):
        """Normal Test 1"""
        self.assertEqual(solution([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5], "Test 1 Failed")

    def test_bubble_sort_test_b(self):
        """Normal Test 2"""
        self.assertEqual(solution([5, 4, 3, 2, 1], 0, 5), [1, 2, 3, 4, 5], "Test 2 Failed")

    def test_bubble_sort_test_c(self):
        """Normal Test 3"""
        self.assertEqual(solution([1, 3, 5, 2, 4], 0, 5), [1, 2, 3, 4, 5], "Test 3 Failed")

    def test_bubble_sort_test_d(self):
        """Normal Test 4"""
        self.assertEqual(solution([1, 3, 5, 2, 4, 6, 8, 7], 0, 5), [1, 2, 3, 4, 5, 6, 7, 8], "Test 4 Failed")

    def test_bubble_sort_test_e(self):
        """Normal Test 5"""
        self.assertEqual(solution([1, 3, 5, 2, 4, 6, 8, 7, 9], 0, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9], "Test 5 Failed")

    def test_bubble_sort_test_f(self):
        """Normal Test 6"""
        self.assertEqual(solution([1, 3, 5, 2, 4, 6, 8, 7, 9, 10], 0, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Test 6 Failed")

    def test_bubble_sort_test_g(self):
        """Normal Test 7"""
        self.assertEqual(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Test 7 Failed")

    def test_bubble_sort_test_h(self):
        """Exception Test 1"""
        self.assertEqual(solution(["b", "c", "l", "a", "z"], 0, 5), ["a", "b", "c", "l", "z"], "Test 8 Failed")

    def test_bubble_sort_test_i(self):
        """Exception Test 2"""
        self.assertEqual(solution(["b", "c", "l", "a", "z", "a", "b", "c", "l", "z"], 0, 10), ["a", "a", "b", "b", "c", "c", "l", "l", "z", "z"], "Test 9 Failed")

    def test_bubble_sort_test_j(self):
        """Exception Test 3"""
        self.assertEqual(solution([], 0, 0), [], "Test 10 Failed")


if __name__ == "__main__":
    unittest.main()
