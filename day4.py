inputRange = "359282-820401"

inputSplit = inputRange.split("-")
inputStart = int(inputSplit[0])
inputEnd = int(inputSplit[1])

okSetA = set()
okSetB = set()


def checkNeighbourA(num):
    listDigit = [int(d) for d in str(num)]
    for ind in range(0, 5):
        if listDigit[ind] == listDigit[ind + 1]:
            return True

    return False


def checkNeighbourB(num):
    listDigit = [int(d) for d in str(num)]
    for ind in range(0, 4):
        if listDigit[ind] == listDigit[ind + 1]:
            if listDigit[ind] == listDigit[ind + 2]:
                return False
            else:
                # print(f"neightbour ok: {num}")
                return True

    return False


def checkDecrasing(num):
    listDigit = [int(d) for d in str(num)]
    for ind in range(0, 5):
        print(f"checking: {listDigit[ind]} {listDigit[ind+1]}")
        if listDigit[ind] > listDigit[ind + 1]:
            return True

    return False


# for num in range(inputStart, inputEnd+1):
#    neigbourA = checkNeighbourA(num)
#    neigbourB = checkNeighbourB(num)
#    decreasing = checkDecrasing(num)

#    if neigbourA and not decreasing:
#       okSetA.add(num)

#    if neigbourB and not decreasing:
#       okSetB.add(num)

print(f"The answer to part A is (511): {len(okSetA)}")
print(f"The answer to part B is: {len(okSetB)}")  # larger than 229
# Test
test1 = "111111"
neighbour = checkNeighbourA(test1)
dec = checkDecrasing(test1)
ok = neighbour and not dec

test2 = "123456"
neighbour2 = checkNeighbourA(test2)
dec2 = checkDecrasing(test2)
ok2 = neighbour2 and not dec2

test3 = "123446"
neighbour3 = checkNeighbourA(test3)
dec3 = checkDecrasing(test3)
ok3 = neighbour3 and not dec3

test4 = "223450"
neighbour4 = checkNeighbourA(test4)
dec4 = checkDecrasing(test4)
ok4 = neighbour4 and not dec4

test5 = "112233"
neighbour5 = checkNeighbourB(test5)
dec5 = checkDecrasing(test4)
ok5 = neighbour5 and not dec5

# print(f"{test1} digits in this string has the same value as their neigbour: {neighbour}")
# print(f"{test1} this string is valid: {ok}")
# print(f"{test2} neightbour false: {neighbour2}, decrasing should be false: {dec2}, this string false: {ok2}")
# print(f"{test3} should be true: {ok3}")
# print(f"{test4} neightbour ok: {neighbour4}, decrasing should be true: {dec4}, this string false: {ok4}")
print(
    f"{test5} neightbour ok: {neighbour5}, decrasing should be false: {dec5}, this string false: {ok5}"
)
