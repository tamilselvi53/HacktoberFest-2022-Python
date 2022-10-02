import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Diamond pattern testcase"""
    def test_diamond_a(self):
        """Normal Test 1"""
        self.assertEqual(solution(3)," * \n***\n * ", "Normal Test 1 Failed")

    def test_diamond_b(self):
        """Normal Test 2"""
        self.assertEqual(solution(5),"  *  \n *** \n*****\n *** \n  *  ", "Normal Test 2 Failed")

    def test_diamond_c(self):
        """Normal Test 3"""
        self.assertEqual(solution(9),"    *    \n   ***   \n  *****  \n ******* \n*********\n ******* \n  *****  \n   ***   \n    *    ", "Normal Test 3 Failed")

    def test_diamond_d(self):
        """Normal Test 4"""
        self.assertEqual(solution(27), "                          *                          \n                         ***                         \n                        *****                        \n                       *******                       \n                      *********                      \n                     ***********                     \n                    *************                    \n                   ***************                   \n                  *****************                  \n                 *******************                 \n                *********************                \n               ***********************               \n              *************************              \n             ***************************             \n            *****************************            \n           *******************************           \n          *********************************          \n         ***********************************         \n        *************************************        \n       ***************************************       \n      *****************************************      \n     *******************************************     \n    *********************************************    \n   ***********************************************   \n  *************************************************  \n *************************************************** \n*****************************************************\n *************************************************** \n  *************************************************  \n   ***********************************************   \n    *********************************************    \n     *******************************************     \n      *****************************************      \n       ***************************************       \n        *************************************        \n         ***********************************         \n          *********************************          \n           *******************************           \n            *****************************            \n             ***************************             \n              *************************              \n               ***********************               \n                *********************                \n                 *******************                 \n                  *****************                  \n                   ***************                   \n                    *************                    \n                     ***********                     \n                      *********                      \n                       *******                       \n                        *****                        \n                         ***                         \n                          *                          ", "Normal Test 4 Failed")

    def test_diamond_e(self):
        """Exception Test 1"""
        self.assertEqual(solution(1),-1, "Exception Test 1 Failed")

    def test_diamond_f(self):
        """Exception Test 2"""
        self.assertEqual(solution(2),-1, "Exception Test 2 Failed")

    def test_diamond_g(self):
        """Exception Test 3"""
        self.assertEqual(solution(4),-1, "Exception Test 3 Failed")

    def test_diamond_h(self):
        """Exception Test 4"""
        self.assertEqual(solution(),-1, "Exception Test 4 Failed")

if __name__ == '__main__':
    unittest.main()