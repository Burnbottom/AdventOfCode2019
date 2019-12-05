def findIncreasing(numbers):
    increasing = []
    for elem in numbers:
        if list(elem) == sorted(elem):
            increasing.append(elem)
    return increasing


def findOkNeigbour(numbers, exact=False):
    okNeigbour = []
    for num in numbers:
        for digit in num:
            count = num.count(digit)
            if exact:
                if count == 2:
                    okNeigbour.append(num)
                    break
            else:
                if count >= 2:
                    okNeigbour.append(num)
                    break
    return okNeigbour


def main():
    result = findOkNeigbour(tmp, True)
    print(f"resut : {result}")
    numbers = []

    # create list of ints with data
    for i in range(359282, 820401):
        numbers.append(str(i))

    increasingOnly = findIncreasing(numbers)

    increaseAndOkNeigbourA = findOkNeigbour(increasingOnly)
    increaseAndOkNeigbourB = findOkNeigbour(increasingOnly, True)
    print(f"Part A, num ok password is: {len(increaseAndOkNeigbourA)}")
    print(f"Part B, num ok password is: {len(increaseAndOkNeigbourB)}")


if __name__ == "__main__":
    main()
