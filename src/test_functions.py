import random
import unittest
import pytest
from parameterized import parameterized, param
import functions


TEST_CASES_COUNT = 10
MIN = -1000
MAX = 1000
TEST_CASES_ARITHMETIC = [
    param(random.randrange(MIN, MAX), random.randrange(MIN, MAX)) for i in range(TEST_CASES_COUNT)
]
TEST_CASES_PRIME = [
    param(1, True), param(2, True), param(3, True), param(4, False), param(5, True),
    param(6, False), param(7, True), param(8, False), param(9, False), param(10, False),
    param(11, True), param(12, False), param(13, True), param(14, False), param(15, False),
    param(16, False), param(17, True), param(18, False), param(19, True), param(20, False),
]
# TEST_CASES_PRIME = [param(i) for i in range(2, TEST_CASES_COUNT)]
pytestmark = pytest.mark.parametrize("arg_1,arg_2", TEST_CASES_ARITHMETIC)


class TestArithmeticFunctions(unittest.TestCase):

    # TEST_CASES_COUNT = 10
    # MIN = -1000
    # MAX = 1000
    # TEST_CASES = []
    # for i in range(TEST_CASES_COUNT):
    #     # TEST_CASES = [(ARGS_1[i], ARGS_2[i]) for i in range(TEST_CASES_COUNT)]
    #     test_case = (random.randrange(MIN, MAX), random.randrange(MIN, MAX))
    #     TEST_CASES.append(test_case)

    @parameterized.expand(TEST_CASES_ARITHMETIC)
    def test_add(self, arg_1, arg_2):
        result_12 = functions.add(arg_1, arg_2)
        result_21 = functions.add(arg_2, arg_1)

        self.assertEqual(result_12, arg_1 + arg_2)
        self.assertEqual(result_21, arg_2 + arg_1)
        self.assertEqual(result_12, result_21)
    

    @parameterized.expand(TEST_CASES_ARITHMETIC)
    def test_subtract(self, arg_1, arg_2):
        result_12 = functions.subtract(arg_1, arg_2)
        result_21 = functions.subtract(arg_2, arg_1)

        self.assertEqual(result_12, arg_1 - arg_2)
        self.assertEqual(result_21, arg_2 - arg_1)
        self.assertEqual(result_12, -result_21)
    

    @parameterized.expand(TEST_CASES_ARITHMETIC)
    def test_multiply(self, arg_1, arg_2):
        result_12 = functions.multiply(arg_1, arg_2)
        result_21 = functions.multiply(arg_2, arg_1)

        self.assertEqual(result_12, arg_1 * arg_2)
        self.assertEqual(result_21, arg_2 * arg_1)
        self.assertEqual(result_12, result_21)
    

    @parameterized.expand([(1, 0)] + TEST_CASES_ARITHMETIC)
    def test_divide(self, arg_1, arg_2):
        if arg_1 == 0 or arg_2 == 0:
            with self.assertRaises(ZeroDivisionError):
                functions.divide(arg_1, arg_2)
                functions.divide(arg_2, arg_1)        
            return

        result_12 = functions.divide(arg_1, arg_2)
        result_21 = functions.divide(arg_2, arg_1)

        self.assertEqual(result_12, arg_1 / arg_2)
        self.assertEqual(result_21, arg_2 / arg_1)
        self.assertNotEqual(result_12, result_21)
    

    @parameterized.expand(TEST_CASES_PRIME)
    def test_is_prime(self, arg, expected_result):
        result = functions.is_prime(arg)
        self.assertTrue(result == expected_result)
            


if __name__ == '__main__':
    unittest.main()