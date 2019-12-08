from day5 import opCodeOperator
from itertools import permutations


def withPermutationA(permutation, inputData):
    # A
    outPutAndModIndataA = opCodeOperator(
        data=inputData, input1=permutation[0], input2=0
    )
    # B
    outPutAndModIndataB = opCodeOperator(
        data=inputData, input1=permutation[1], input2=outPutAndModIndataA[0][-1]
    )
    # C
    outPutAndModIndataC = opCodeOperator(
        data=inputData, input1=permutation[2], input2=outPutAndModIndataB[0][-1]
    )
    # D
    outPutAndModIndataD = opCodeOperator(
        data=inputData, input1=permutation[3], input2=outPutAndModIndataC[0][-1]
    )
    # E
    outPutAndModIndataE = opCodeOperator(
        data=inputData, input1=permutation[4], input2=outPutAndModIndataD[0][-1]
    )

    return outPutAndModIndataE[0]


def updateOutout(outputold, outputNew):
    if outputNew != []:
        return outputNew[-1]
    else:
        return outputold


def withPermutationB(permutation, input):
    initA = False
    initB = False
    initC = False
    initD = False
    initE = False

    dataA = input
    dataB = input
    dataC = input
    dataD = input
    dataE = input

    posIterA = None
    posIterB = None
    posIterC = None
    posIterD = None
    posIterE = None
    output = 0
    while True:
        # A
        outPutAndModIndataA = opCodeOperator(
            data=dataA,
            input1=permutation[0],
            input2=output,
            initalized=initA,
            instStartInd=posIterA,
        )
        output = updateOutout(output, outPutAndModIndataA[0])
        dataA = outPutAndModIndataA[1]
        posIterA = outPutAndModIndataA[2]
        # B
        outPutAndModIndataB = opCodeOperator(
            data=dataB,
            input1=permutation[1],
            input2=output,
            initalized=initB,
            instStartInd=posIterB,
        )
        output = updateOutout(output, outPutAndModIndataB[0])
        dataB = outPutAndModIndataB[1]
        posIterB = outPutAndModIndataB[2]
        # C
        outPutAndModIndataC = opCodeOperator(
            data=dataC,
            input1=permutation[2],
            input2=output,
            initalized=initC,
            instStartInd=posIterC,
        )
        output = updateOutout(output, outPutAndModIndataC[0])
        dataC = outPutAndModIndataC[1]
        posIterC = outPutAndModIndataC[2]
        # D
        outPutAndModIndataD = opCodeOperator(
            data=dataD,
            input1=permutation[3],
            input2=output,
            initalized=initD,
            instStartInd=posIterD,
        )
        output = updateOutout(output, outPutAndModIndataD[0])
        dataD = outPutAndModIndataD[1]
        posIterD = outPutAndModIndataD[2]
        # E
        outPutAndModIndataE = opCodeOperator(
            data=dataE,
            input1=permutation[4],
            input2=output,
            initalized=initE,
            instStartInd=posIterE,
        )
        output = updateOutout(output, outPutAndModIndataE[0])
        dataE = outPutAndModIndataD[1]
        posIterE = outPutAndModIndataD[2]
        if outPutAndModIndataE[0] == []:
            return output


input = "3,8,1001,8,10,8,105,1,0,0,21,30,47,60,81,102,183,264,345,426,99999,3,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,102,4,9,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99"
input = [int(d) for d in input.split(",")]
bestComboA = ()
maxThrustA = 0
for combo in permutations(range(0, 5)):
    out = withPermutationA(combo, input)
    if out[-1] > maxThrustA:
        maxThrustA = out[-1]
        bestComboA = combo

bestComboB = ()
maxThrustB = 0
for combo in permutations(range(5, 10)):
    out = withPermutationB(combo, input)
    if out > maxThrustB:
        maxThrustB = out
        bestComboB = combo

print(f"Part A: max Thrust {maxThrustA}, permutaion {bestComboA}")
print(f"Part B: max Thrust {maxThrustB}, permutaion {bestComboB}")
