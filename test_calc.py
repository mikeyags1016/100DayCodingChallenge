import unittest
import calculator


class TestCalc(unittest.TestCase):

    def test_operators(self):
        self.assertEqual(calculator.equation_definer("+", 3, 4), 7)
        self.assertEqual(calculator.equation_definer("-", 4, 2), 2)
        self.assertEqual(calculator.equation_definer("*", 3, 4), 12)
        self.assertEqual(calculator.equation_definer("/", 12, 4), 3)
        self.assertEqual(calculator.equation_definer("%", 12, 4), 0)
        self.assertEqual(calculator.equation_definer("**", 2, 0), 1)

    def invalid(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.division(5, 0)
            calculator.modulus(5, 0)


if __name__ == "__main__":
    unittest.main()
