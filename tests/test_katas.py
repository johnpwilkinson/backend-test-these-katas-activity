import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2,2), 4)
        self.assertEqual(katas.add(-2,-1), -3)


    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 3), 6)
        self.assertEqual(katas.multiply(-2,-1), 2)

    def test_power(self):
        self.assertEqual(katas.power(2, 2), 4)
        self.assertEqual(katas.power(10,2), 100)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(10), 3628800)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 3)
        self.assertEqual(katas.fibonacci(7), 8)

if __name__ == '__main__':
    unittest.main()