import unittest

from EP1 import view_result_sum_of_multiples_below_borne

class Test_view_result_sum_of_multiples_below_borne(unittest.TestCase):
    def test_0(self):
        self.assertEqual(view_result_sum_of_multiples_below_borne([3, 5], 10),\
        "The sum of multiples of 3, 5 below 10 is : 23")
    def test_1(self):
        self.assertEqual(view_result_sum_of_multiples_below_borne([], 10),\
        'Some inputs were invalids | List is empty')
            
    def test_2(self):
        self.assertEqual(view_result_sum_of_multiples_below_borne([3, 5], 1),\
        'Some inputs were invalids | Borne < 2')
            
    def test_3(self):
        self.assertEqual(view_result_sum_of_multiples_below_borne([-1, 5], 10),\
        'Some inputs were invalids | Numbers in list must be strictly positive')
            
    def test_4(self):
        self.assertEqual(view_result_sum_of_multiples_below_borne([1, -5], 10),\
        'Some inputs were invalids | Numbers in list must be strictly positive')
            

if __name__ == "__main__":
    unittest.main()
