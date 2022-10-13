import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Binary to decimal Test"""
    def test_binary_to_decimal_test_a(self):
        """Normal Test 1"""
        self.assertEqual(solution(1010), 10, "Test 1 Failed")

    def test_binary_to_decimal_test_b(self):
        """Normal Test 2"""
        self.assertEqual(solution(1011), 11, "Test 2 Failed")

    def test_binary_to_decimal_test_c(self):
        """Normal Test 3"""
        self.assertEqual(solution(1001), 9, "Test 3 Failed")

    def test_binary_to_decimal_test_d(self):
        """Normal Test 4"""
        self.assertEqual(solution(10101001), 169, "Test 4 Failed")

    def test_binary_to_decimal_test_e(self):
        """Normal Test 5"""
        self.assertEqual(solution(111111111111111111111111111111), 4294967295, "Test 5 Failed")

    def test_binary_to_decimal_test_f(self):
        """Normal Test 6"""
        self.assertEqual(solution(1111111111111111111111111111111), 8589934591, "Test 6 Failed")

    def test_binary_to_decimal_test_g(self):
        "Exception Test 1"""
        self.assertEqual(solution(), -1, "Test 7 Failed")

    def test_binary_to_decimal_test_h(self):
        """Exception Test 2"""
        self.assertEqual(solution(123), -1, "Test 8 Failed")

    def test_binary_to_decimal_test_i(self):
        """Exception Test 3"""
        self.assertEqual(solution(123456789), -1, "Test 9 Failed")

    def test_binary_to_decimal_test_j(self):
        """Exception Test 4"""
        self.assertEqual(solution("1010"), 10, "Test 10 Failed")


if __name__ == "__main__":
    utility.main()
