from itertools import product

from computer import Computer


def opCodeOperator(data, firstPosUpdate=None, secondPosUpdate=None):
    # copy
    inputData = data.copy()
    if firstPosUpdate != None:
        inputData[1] = firstPosUpdate
    if secondPosUpdate != None:
        inputData[2] = secondPosUpdate
    for opCodePos in range(0, len(inputData), 4):
        if inputData[opCodePos] == 99:
            return inputData
        elif inputData[opCodePos] == 1:
            inputData[inputData[opCodePos + 3]] = (
                inputData[inputData[opCodePos + 1]]
                + inputData[inputData[opCodePos + 2]]
            )
        elif inputData[opCodePos] == 2:
            inputData[inputData[opCodePos + 3]] = (
                inputData[inputData[opCodePos + 1]]
                * inputData[inputData[opCodePos + 2]]
            )
        else:
            raise ValueError(f"Unknown opCode: {inputData[opCodePos]}")

    return inputData


def main():
    # updated input
    # input = "1,12,2,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,10,19,23,2,9,23,27,1,6,27,31,2,31,9,35,1,5,35,39,1,10,39,43,1,10,43,47,2,13,47,51,1,10,51,55,2,55,10,59,1,9,59,63,2,6,63,67,1,5,67,71,1,71,5,75,1,5,75,79,2,79,13,83,1,83,5,87,2,6,87,91,1,5,91,95,1,95,9,99,1,99,6,103,1,103,13,107,1,107,5,111,2,111,13,115,1,115,6,119,1,6,119,123,2,123,13,127,1,10,127,131,1,131,2,135,1,135,5,0,99,2,14,0,0"
    input = "1,9,10,3,2,3,11,0,99,30,40,50"
    inputList = [int(d) for d in input.split(",")]

    # part A
    computerA = Computer(inputList)
    outputA = computerA.run()
    print(outputA)


# def main():
#    input = "1,,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,10,19,23,2,9,23,27,1,6,27,31,2,31,9,35,1,5,35,39,1,10,39,43,1,10,43,47,2,13,47,51,1,10,51,55,2,55,10,59,1,9,59,63,2,6,63,67,1,5,67,71,1,71,5,75,1,5,75,79,2,79,13,83,1,83,5,87,2,6,87,91,1,5,91,95,1,95,9,99,1,99,6,103,1,103,13,107,1,107,5,111,2,111,13,115,1,115,6,119,1,6,119,123,2,123,13,127,1,10,127,131,1,131,2,135,1,135,5,0,99,2,14,0,0"
#    inputList = [int(d) for d in input.split(",")]
#
#    # part 1
#    updatedData = opCodeOperator(inputList, 12, 2)
#    print(f"answer to part 1 is: {updatedData[0]}")
#
#    # part 2
#    for noun, verb in product(range(0, 100), range(0, 100)):
#        if opCodeOperator(inputList, noun, verb)[0] == 19690720:
#            print(
#                f"noun is {noun}, verb is {verb}, the number seeked (100*noun + verb) is: {100*noun + verb}"
#            )


if __name__ == "__main__":
    main()
