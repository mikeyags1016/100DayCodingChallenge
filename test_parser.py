import unittest
import parser


class TestParser(unittest.TestCase):
    def test_parser(self):
        filepath = 'data.txt'
        data = parser.parse_file(filepath)
        print(data)


if __name__ == '__main__':
    unittest.main()