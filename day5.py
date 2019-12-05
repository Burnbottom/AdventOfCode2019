from enum import Enum


class ParameterMode(Enum):
    Position = 1
    Immediate = 2


def paddIfNessecary(instruction):
    length = len(instruction)

    return (instruction.zfill(5), 5 - length)


# return Opcode, mode of 1 param, mode of 2 param, mode of 3 param
def parseInstruction(instruction):
    return [instruction[3:], instruction[2], instruction[1], instruction[0]]


def opCodeOperator(data, firstPosUpdate=None, secondPosUpdate=None, input=None):
    # copy
    inputData = data.copy()

    if firstPosUpdate != None:
        inputData[1] = firstPosUpdate
    if secondPosUpdate != None:
        inputData[2] = secondPosUpdate

    for instructionStartIndex in range(0, len(data) + 1):
        instruction = inputData[inputData[instructionStartIndex]]
        paddedFirst, numPadding = paddIfNessecary(instruction)
        parsedInstruction = parseInstruction(paddedFirst)

        opCode = parsedInstruction[0]
        modeFirst = parsedInstruction[1]
        modeSecond = parsedInstruction[2]
        modeThird = parsedInstruction[3]
        # Reset values if padded was neccesary, maybe unncessasary
        if numPadding == 2:
            modeSecond = None
            modeThird = None
        elif numPadding == 1:
            modeThird = None

        while opCode != 99:
            if opCode == 1:  # adding
                # will take a total of 4 elements for input data
                instructionStartIndex += 4
                value1 = (
                    inputData[inputData[instructionStartIndex + 1]]
                    if modeFirst == ParameterMode.Position
                    else instructionStartIndex + 1
                )
                value2 = (
                    inputData[inputData[instructionStartIndex + 2]]
                    if modeSecond == ParameterMode.Position
                    else instructionStartIndex + 2
                )
                insertPos = (
                    inputData[instructionStartIndex + 3]
                    if modeThird == ParameterMode.Position
                    else instructionStartIndex + 3
                )
                inputData[insertPos] = value1 + value2
            elif opCode == 2:
                instructionStartIndex += 4
                value1 = (
                    inputData[inputData[instructionStartIndex + 1]]
                    if modeFirst == ParameterMode.Position
                    else instructionStartIndex + 1
                )
                value2 = (
                    inputData[inputData[instructionStartIndex + 2]]
                    if modeSecond == ParameterMode.Position
                    else instructionStartIndex + 2
                )
                insertPos = (
                    inputData[instructionStartIndex + 3]
                    if modeThird == ParameterMode.Position
                    else instructionStartIndex + 3
                )
                inputData[insertPos] = value1 * value2
            elif opCode == 3:
                instructionStartIndex += 2
                insertPos = (
                    inputData[instructionStartIndex + 1]
                    if modeThird == ParameterMode.Position
                    else instructionStartIndex + 1
                )
                inputData[inputData[insertPos]] = input
            elif opCode == 4:
                instructionStartIndex += 2
                insertPos = (
                    inputData[instructionStartIndex + 1]
                    if modeThird == ParameterMode.Position
                    else instructionStartIndex + 1
                )
                print(inputData[inputData[insertPos]])
            else:
                raise ValueError(f"Unknown opCode: {opCode}")
        return inputData


def main():
    inputData = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,40,27,224,101,-67,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,33,38,225,1102,84,60,225,1101,65,62,225,1002,36,13,224,1001,224,-494,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,86,5,224,101,-430,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,23,50,225,1001,44,10,224,101,-72,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,102,47,217,224,1001,224,-2303,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,71,84,225,101,91,40,224,1001,224,-151,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,87,91,225,1102,71,19,225,1,92,140,224,101,-134,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,2,170,165,224,1001,224,-1653,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,49,32,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,677,224,1002,223,2,223,1006,224,329,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,344,101,1,223,223,1007,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,374,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,434,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,509,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,539,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,569,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,584,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226"
    inputList = inputData.split(",")

    input = 1

    opCodeOperator(data=inputList, input=input)


if __name__ == "__main__":
    main()
