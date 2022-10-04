import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    "Binary Search Test"
    def test_binary_search_test_a(self):
        "Normal Test 1"
        self.assertEqual(solution([1, 2, 6, 0, 5], 3), 2, "Test 1 Failed")

    def test_binary_search_test_b(self):
        "Normal Test 2"
        self.assertEqual(solution([9, 4, 3, 8, 5], 5), 4, "Test 2 Failed")

    def test_binary_search_test_c(self):
        "Normal Test 3"
        self.assertEqual(solution([1, 2, 7, 10, 8], 1), 0, "Test 3 Failed")

    def test_binary_search_test_d(self):
        "Normal Test 4"
        self.assertEqual(solution([8, 15, 3, 4, 5], 0), -1, "Test 4 Failed")

    def test_binary_search_test_e(self):
        "Normal Test 5"
        self.assertEqual(solution([21, 92, 8, 14, 5], 6), -1, "Test 5 Failed")

    def test_binary_search_test_i(self):
        "Exception Test 1"
        self.assertEqual(solution(), -1, "Test 6 Failed")

    def test_binary_search_test_j(self):
        "Exception Test 2"
        self.assertEqual(solution(1), -1, "Test 7 Failed")

    def test_binary_search_test_k(self):
        "Exception Test 3"
        self.assertEqual(solution("a"), -1, "Test 8 Failed")

    def test_binary_search_test_l(self):
        "Exception Test 4"
        self.assertEqual(solution(1.5), -1, "Test 9 Failed")


if __name__ == "__main__":
    utility.main()
