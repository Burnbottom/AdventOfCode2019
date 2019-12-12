from itertools import combinations
import math


def calcVel(pos1, pos2):
    val1 = 0
    val2 = 0
    if pos1 > pos2:
        val1 = -1
        val2 = 1
    elif pos1 < pos2:
        val1 = 1
        val2 = -1
    return (val1, val2)


def updateVel(firstMoon, secondMoon):
    x1, x2 = calcVel(firstMoon.xPos, secondMoon.xPos)
    firstMoon.xVel += x1
    secondMoon.xVel += x2

    y1, y2 = calcVel(firstMoon.yPos, secondMoon.yPos)
    firstMoon.yVel += y1
    secondMoon.yVel += y2

    z1, z2 = calcVel(firstMoon.zPos, secondMoon.zPos)
    firstMoon.zVel += z1
    secondMoon.zVel += z2


def updatePos(moon):
    moon.xPos += moon.xVel
    moon.yPos += moon.yVel
    moon.zPos += moon.zVel


def printMoonValue(moon):
    print(
        f"pos: {moon.xPos} {moon.yPos} {moon.zPos}, vel: {moon.xVel} {moon.yVel} {moon.zVel}"
    )


def calctotEnergy(steps, moonList):
    totEnergy = 0
    for _ in range(steps):
        comb = combinations(range(len(moonList)), 2)
        for c in comb:
            updateVel(moonList[c[0]], moonList[c[1]])

        for moon in moonList:
            updatePos(moon)

    for moon in moonList:
        kinE = moon.calcKinEnergy()
        potE = moon.calcPotEnergy()
        totEnergy += kinE * potE

    return totEnergy


def calcLCM(num1, num2):
    return (num1 * num2) // math.gcd(num1, num2)


class Moon:
    def __init__(self, xPos, yPos, zPos):
        self.xPos = int(xPos)
        self.yPos = int(yPos)
        self.zPos = int(zPos)

        self.xVel = 0
        self.yVel = 0
        self.zVel = 0

        self.cycleLen = 0

    def calcPotEnergy(self):
        return abs(self.xPos) + abs(self.yPos) + abs(self.zPos)

    def calcKinEnergy(self):
        return abs(self.xVel) + abs(self.yVel) + abs(self.zVel)


moonList = []
input = open("init12.txt", "r")
for row in input:
    row = row.strip("\n")
    row = row.replace(" ", "")
    row = row[1:-1]
    parts = row.split(",")
    moon = Moon(parts[0][2:], parts[1][2:], parts[2][2:])
    moonList.append(moon)
input.close()


a = calctotEnergy(1000, moonList.copy())
print(f"Part A: {a}")

"""
while True:
    comb = combinations(range(len(moonList)), 2)
    origValues = moonList.copy()
    for c in comb:
        updateVel(moonList[c[0]], moonList[c[1]])

    for moon in moonList:
        updatePos(moon)


    break
"""
