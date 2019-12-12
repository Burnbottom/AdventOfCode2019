import unittest
from day12 import Moon, calctotEnergy


class TestMethods(unittest.TestCase):
    def test1(self):
        moonList = []
        moonA = Moon(-1, 0, 2)
        moonB = Moon(2, -10, -7)
        moonC = Moon(4, -8, 8)
        moonD = Moon(3, 5, -1)

        moonList.append(moonA)
        moonList.append(moonB)
        moonList.append(moonC)
        moonList.append(moonD)

        out = calctotEnergy(10, moonList.copy())
        self.assertEqual(179, out)

    def test2(self):
        moonList = []
        moonA = Moon(-8, -10, 0)
        moonB = Moon(5, 5, 10)
        moonC = Moon(2, -7, 3)
        moonD = Moon(9, -8, -3)

        moonList.append(moonA)
        moonList.append(moonB)
        moonList.append(moonC)
        moonList.append(moonD)

        out = calctotEnergy(100, moonList.copy())
        self.assertEqual(1940, out)

    def test3(self):
        moonList = []
        moonA = Moon(-15, 1, 4)
        moonB = Moon(1, -10, -8)
        moonC = Moon(-5, 4, 9)
        moonD = Moon(4, 6, -2)

        moonList.append(moonA)
        moonList.append(moonB)
        moonList.append(moonC)
        moonList.append(moonD)

        out = calctotEnergy(1000, moonList.copy())
        self.assertEqual(8625, out)


if __name__ == "__main__":
    unittest.main()
