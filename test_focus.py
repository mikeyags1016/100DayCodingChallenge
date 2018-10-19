import unittest
import focus


class TestFocus(unittest.TestCase):
    def test_stage(self):
        self.assertEqual(focus.stage(6), 'Grandfather tree')

    def test_invalid(self):
        with self.assertRaises(AssertionError):
            focus.stage(7)


if __name__ == "__main__":
    unittest.main()