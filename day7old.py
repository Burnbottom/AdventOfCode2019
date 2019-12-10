import numpy as np

from day5 import opCodeOperator, getLastVal
from itertools import permutations


def withPermutation(permutation, inputData):
    if not isinstance(permutation, list):
        permutation = list(permutation)
    output = 0
    while len(permutation) > 0:
        # A
        output = opCodeOperator(
            data=inputData, input1=permutation.pop(0), input2=output
        )
        # B
        output = opCodeOperator(
            data=inputData, input1=permutation.pop(0), input2=next(output)
        )
        # C
        output = opCodeOperator(
            data=inputData, input1=permutation.pop(0), input2=next(output)
        )
        # D
        output = opCodeOperator(
            data=inputData, input1=permutation.pop(0), input2=next(output)
        )
        # E
        output = opCodeOperator(
            data=inputData, input1=permutation.pop(0), input2=next(output)
        )
        output = next(output)
        yield output


def part_one(inputData, permIter):
    bestPerm = ()
    maxThrust = 0

    for perm in permIter:
        out = withPermutation(perm, inputData)
        output = next(out)
        if output > maxThrust:
            maxThrust = output
            bestPerm = perm
    return (maxThrust, bestPerm)


input = "3,8,1001,8,10,8,105,1,0,0,21,30,47,60,81,102,183,264,345,426,99999,3,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,102,4,9,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99"
input = [int(d) for d in input.split(",")]

partA = part_one(input, permutations(range(5)))
print(f"Part A: max Thrust {partA[0]}, permutaion {partA[1]}")
# partB = feedbackLoop(input, permutations(range(5)), withPermutation)
# print(partB)
