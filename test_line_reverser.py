import unittest
import line_reverser


class test_line_reverser(unittest.TestCase):
    def setUp(cls):
        cls.text1 = "palindrome"
        cls.result1 = cls.text1[::-1]
        cls.text2 = "racecar"
        cls.result2 = cls.text2[::-1]
        cls.text3 = "A"
        cls.result3 = cls.text3[::-1]

    def test_line_reverser(self):
        self.assertEqual(line_reverser.reverse_string(self.text1), self.result1)
        self.assertEqual(line_reverser.reverse_string(self.text2), self.result2)
        self.assertEqual(line_reverser.reverse_string(self.text3), self.result3)


if __name__ == '__main__':
    unittest.main()
