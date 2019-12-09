from enum import Enum

Position = 0
Immediate = 1


def opCodeOperator(
    data, firstPosUp=None, secondPosUp=None, input1=None, input2=None, init=False,
):
    output = []
    inputData = data.copy()

    if firstPosUp != None:
        inputData[1] = firstPosUp
    if secondPosUp != None:
        inputData[2] = secondPosUp

    instStartInd = 0

    while inputData[instStartInd] != 99:
        instruction = inputData[instStartInd]

        opCode = instruction % 100
        modeFirst = instruction // 100 % 10
        modeSecond = instruction // 1000 % 10
        modeThird = instruction // 10000 % 10

        position1 = (
            inputData[instStartInd + 1] if modeFirst == Position else instStartInd + 1
        )
        position2 = (
            inputData[instStartInd + 2] if modeSecond == Position else instStartInd + 2
        )
        if opCode == 1:  # adding
            position3 = (
                inputData[instStartInd + 3]
                if modeThird == Position
                else instStartInd + 3
            )
            inputData[position3] = inputData[position1] + inputData[position2]
            instStartInd += 4
        elif opCode == 2:  # multiplying
            position3 = (
                inputData[instStartInd + 3]
                if modeThird == Position
                else instStartInd + 3
            )
            inputData[position3] = inputData[position1] * inputData[position2]
            instStartInd += 4
        elif opCode == 3:  # insert
            if input2 == None:
                tmp = input1
            else:
                if init == False:
                    init = True
                    tmp = input1
                else:
                    tmp = input2
            inputData[position1] = tmp
            instStartInd += 2
        elif opCode == 4:  # output
            output = inputData[position1]
            instStartInd += 2
            yield output
        elif opCode == 5:  # Jump if true
            if inputData[position1] != 0:
                instStartInd = inputData[position2]
            else:
                instStartInd += 3
        elif opCode == 6:  # Jump if false
            if inputData[position1] == 0:
                instStartInd = inputData[position2]
            else:
                instStartInd += 3
        elif opCode == 7:
            position3 = (
                inputData[instStartInd + 3]
                if modeThird == Position
                else instStartInd + 3
            )
            if inputData[position1] < inputData[position2]:
                inputData[position3] = 1
            else:
                inputData[position3] = 0
            instStartInd += 4
        elif opCode == 8:
            position3 = (
                inputData[instStartInd + 3]
                if modeThird == Position
                else instStartInd + 3
            )
            if inputData[position1] == inputData[position2]:
                inputData[position3] = 1
            else:
                inputData[position3] = 0
            instStartInd += 4
        else:
            raise ValueError(f"Unknown opCode: {opCode}")
    print("halting")
    yield None


def getLastVal(genIter):
    last = None
    for e in genIter:
        last = e
    return last


def main():
    inputData = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,40,27,224,101,-67,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,33,38,225,1102,84,60,225,1101,65,62,225,1002,36,13,224,1001,224,-494,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,86,5,224,101,-430,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,23,50,225,1001,44,10,224,101,-72,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,102,47,217,224,1001,224,-2303,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,71,84,225,101,91,40,224,1001,224,-151,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,87,91,225,1102,71,19,225,1,92,140,224,101,-134,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,2,170,165,224,1001,224,-1653,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,49,32,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,677,224,1002,223,2,223,1006,224,329,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,344,101,1,223,223,1007,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,374,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,434,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,509,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,539,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,569,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,584,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226"
    inputData = [int(d) for d in inputData.split(",")]
    print(f"answer part 1: {getLastVal(opCodeOperator(data=inputData, input1=1))}")
    print(f"answer part 2: {getLastVal(opCodeOperator(data=inputData, input1=5))}")


if __name__ == "__main__":
    main()
