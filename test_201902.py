import unittest
from computer import Computer
from itertools import product
from day2 import opCodeOperator


class TestMethods(unittest.TestCase):
    def test1(self):
        input = "1,9,10,3,2,3,11,0,99,30,40,50"
        inputList = [int(d) for d in input.split(",")]
        updatedData = Computer(inputList).run()
        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50], updatedData)

    def test2(self):
        input = "1,0,0,0,99"
        inputList = [int(d) for d in input.split(",")]
        updatedData = Computer(inputList).run()
        self.assertEqual([2, 0, 0, 0, 99], updatedData)

    def test3(self):
        input = "2,3,0,3,99"
        inputList = [int(d) for d in input.split(",")]
        updatedData = Computer(inputList).run()
        self.assertEqual([2, 3, 0, 6, 99], updatedData)

    def test4(self):
        input = "2,4,4,5,99,0"
        inputList = [int(d) for d in input.split(",")]
        updatedData = Computer(inputList).run()
        self.assertEqual([2, 4, 4, 5, 99, 9801], updatedData)

    def test5(self):
        input = "1,1,1,4,99,5,6,0,99"
        inputList = [int(d) for d in input.split(",")]
        updatedData = Computer(inputList).run()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], updatedData)

    # test input data for part A
    def test6(self):
        input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,10,19,23,2,9,23,27,1,6,27,31,2,31,9,35,1,5,35,39,1,10,39,43,1,10,43,47,2,13,47,51,1,10,51,55,2,55,10,59,1,9,59,63,2,6,63,67,1,5,67,71,1,71,5,75,1,5,75,79,2,79,13,83,1,83,5,87,2,6,87,91,1,5,91,95,1,95,9,99,1,99,6,103,1,103,13,107,1,107,5,111,2,111,13,115,1,115,6,119,1,6,119,123,2,123,13,127,1,10,127,131,1,131,2,135,1,135,5,0,99,2,14,0,0"
        inputList = [int(d) for d in input.split(",")]
        updatedData = Computer(inputList).run()
        self.assertEqual(3760627, updatedData[0])

    # test input data for part b
    def test7(self):
        input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,10,19,23,2,9,23,27,1,6,27,31,2,31,9,35,1,5,35,39,1,10,39,43,1,10,43,47,2,13,47,51,1,10,51,55,2,55,10,59,1,9,59,63,2,6,63,67,1,5,67,71,1,71,5,75,1,5,75,79,2,79,13,83,1,83,5,87,2,6,87,91,1,5,91,95,1,95,9,99,1,99,6,103,1,103,13,107,1,107,5,111,2,111,13,115,1,115,6,119,1,6,119,123,2,123,13,127,1,10,127,131,1,131,2,135,1,135,5,0,99,2,14,0,0"
        inputList = [int(d) for d in input.split(",")]
        for noun, verb in product(range(0, 100), range(0, 100)):
            if opCodeOperator(inputList, noun, verb)[0] == 19690720:
                self.assertEqual(71, noun)
                self.assertEqual(95, verb)


if __name__ == "__main__":
    unittest.main()
