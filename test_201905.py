import unittest
from day5 import paddIfNessecary


class TestMethods(unittest.TestCase):
    def testPadding(self):
        answer = paddIfNessecary("123")
        self.assertEqual("00123", str(answer))


if __name__ == "__main__":
    unittest.main()
