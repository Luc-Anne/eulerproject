import unittest

from utils.sum_of_multiples_of_a_list_of_numbers_below_b import sum_of_multiples_of_a_list_of_numbers_below_b
from utils.sum_of_multiples_of_a_list_of_numbers_below_b import sum_of_multiples_of_n_below_b
from utils.sum_of_multiples_of_a_list_of_numbers_below_b import check_sum_of_multiples_of_a_list_of_numbers_below_b

class Test_sum_of_multiples_of_a_list_of_numbers_below_b(unittest.TestCase):
    def test_0(self):
        self.assertEqual(sum_of_multiples_of_a_list_of_numbers_below_b([3, 5], 10),\
        [True, float(3+6+9+5)])
    # Result must not change dependings on numbers' order
    def test_1(self):
        self.assertEqual(sum_of_multiples_of_a_list_of_numbers_below_b([6, 3], 10),\
        sum_of_multiples_of_a_list_of_numbers_below_b([3, 6], 10))
    # Number of the list which are multiple of others must not be count
    def test_2(self):
        self.assertEqual(sum_of_multiples_of_a_list_of_numbers_below_b([3, 5, 15], 20),
        sum_of_multiples_of_a_list_of_numbers_below_b([3, 5], 20))
        self.assertEqual(sum_of_multiples_of_a_list_of_numbers_below_b([3, 5, 15, 45], 100),
        sum_of_multiples_of_a_list_of_numbers_below_b([3, 5], 100))
        self.assertEqual(sum_of_multiples_of_a_list_of_numbers_below_b([3, 15, 5, 45], 100),
        sum_of_multiples_of_a_list_of_numbers_below_b([3, 5], 100))
    # Multiples must be added only one time
    def test_3(self):
        self.assertEqual(sum_of_multiples_of_a_list_of_numbers_below_b([2, 3], 10),
        [True, float(2+4+6+8 + 3+0+9)])

class Test_sum_of_multiples_of_n_below_b(unittest.TestCase):
    def test_0(self):
        self.assertEqual(sum_of_multiples_of_n_below_b(3, 10),\
        float(3+6+9))
    # Multiple egals to borne must not be added
    def test_1(self):
        self.assertEqual(sum_of_multiples_of_n_below_b(5, 10),\
        float(5))
    # n > borne must be egal to 0
    def test_2(self):
        self.assertEqual(sum_of_multiples_of_n_below_b(50, 10),\
        float(0))
    # n = borne must be egal to 0
    def test_3(self):
        self.assertEqual(sum_of_multiples_of_n_below_b(10, 10),\
        float(0))

class Test_check_sum_of_multiples_of_a_list_of_numbers_below_b(unittest.TestCase):
    def test_0(self):
        self.assertEqual(check_sum_of_multiples_of_a_list_of_numbers_below_b([], 10),\
        (False, 0, 'sum_of_multiples_of_a_list_of_numbers_below_b', 'List is empty'))
    def test_1(self):
        self.assertEqual(check_sum_of_multiples_of_a_list_of_numbers_below_b([3, 1, 3, 5], 10),\
        (False, 0, 'sum_of_multiples_of_a_list_of_numbers_below_b', 'There are doublons in list'))
    def test_2(self):
        self.assertEqual(check_sum_of_multiples_of_a_list_of_numbers_below_b([3, 5], 1),\
        (False, 0, 'sum_of_multiples_of_a_list_of_numbers_below_b', 'Borne < 2'))
    def test_3(self):
        self.assertEqual(check_sum_of_multiples_of_a_list_of_numbers_below_b([-1, 5], 10),\
        (False, 0, 'sum_of_multiples_of_a_list_of_numbers_below_b', 'Numbers in list must be strictly positive'))
        self.assertEqual(check_sum_of_multiples_of_a_list_of_numbers_below_b([1, -5], 10),\
        (False, 0, 'sum_of_multiples_of_a_list_of_numbers_below_b', 'Numbers in list must be strictly positive'))

if __name__ == "__main__":
    unittest.main()
