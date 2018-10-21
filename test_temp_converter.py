import unittest
from temp_converter import TempConverter


class TestTempConverter(unittest.TestCase):
    def setUp(self):
        self.temp = TempConverter()

    def test_convert_fahr(self):
        self.assertEqual(self.temp.convert_to_fahrenheit(100, 'c'), 212)
        self.assertEqual(self.temp.convert_to_fahrenheit(100, 'k'), -279.66999999999996)

    def test_convert_celc(self):
        self.assertEqual(self.temp.convert_to_celcius(32, 'f'), 0)
        self.assertEqual(self.temp.convert_to_celcius(32, 'k'), -241.14999999999998)

    def test_convert_kel(self):
        self.assertEqual(self.temp.convert_to_kelvin(100, 'f'), 310.92777777777775)
        self.assertEqual(self.temp.convert_to_kelvin(-272.15, 'c'), 1)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            self.temp.convert_to_fahrenheit(100, 'f')
            self.temp.convert_to_celcius(100, 'c')
            self.temp.convert_to_kelvin(100, 'f')
            self.temp.convert_to_kelvin('A', 'f')


if __name__ == "__main__":
    unittest.main()