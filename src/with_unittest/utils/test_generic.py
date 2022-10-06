import unittest

from utils.generic import copy_list

class Test_copy_list(unittest.TestCase):
    def test_0(self):
        input_list = [-1, 2, 3]
        list = copy_list([-1, 2, 3])
        self.assertEqual(list, input_list)

if __name__ == "__main__":
    unittest.main()
