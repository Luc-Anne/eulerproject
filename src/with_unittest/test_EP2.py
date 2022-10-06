import unittest

from EP2 import fibonacci_serie_generator
from EP2 import sum_of_even_fibonacci_borne2

class Test_fibonacci_serie_generator(unittest.TestCase):
    def test_0(self):
        gen = fibonacci_serie_generator()
        fib = []
        for i in gen:
            fib.append(i)
            if len(fib) > 9:
                break
        self.assertEqual(fib, [1,2,3,5,8,13,21,34,55,89])
        return fib
    def test_1(self):
        fib = self.test_0()
        sum = 0
        for i in range(len(fib)):
            if fib[i] % 2 == 0:
                sum += fib[i]
        self.assertEqual(sum_of_even_fibonacci_borne2(100), sum)

if __name__ == "__main__":
    unittest.main()
