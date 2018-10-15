import unittest
import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fibonacci.fib(14), 377)
        self.assertEqual(fibonacci.fib(1), 1)
        self.assertEqual(fibonacci.fib(2), 1)
        self.assertEqual(fibonacci.fib(0), 1)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            fibonacci.fib(3.14)
            fibonacci.fib(-1)
        with self.assertRaises(ValueError):
            fibonacci.fib("A")


if __name__ == "__main__":
    unittest.main()
