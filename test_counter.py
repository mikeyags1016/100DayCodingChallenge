import unittest
import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fibonacci.fibonacci(14), 377)
        self.assertEqual(fibonacci.fibonacci(1), 1)
        self.assertEqual(fibonacci.fibonacci(2), 1)
        self.assertEqual(fibonacci.fibonacci(0), 1)

    def test_invalid(self):
        self.assertEqual(fibonacci.fibonacci(-1), -1)
        self.assertEqual(fibonacci.fibonacci(3.14), -1)

        with self.assertRaises(ValueError):
            fibonacci.fibonacci("A")


if __name__ == "__main__":
    unittest.main()