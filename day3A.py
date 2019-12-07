import numpy as np

input = open("data3.txt", "r")
mapOfWire = {}
wire_id = 1


def calculateManhattanDistance(intersectPoint):
    return abs(intersectPoint[0] - 0) + abs(intersectPoint[1] - 0)


def splitAction(action):
    return (action[0], action[1:])


def addOrUpdateMap(coord, wire_id, stepsTaken):
    if coord in mapOfWire:
        wireIdAndSteps = mapOfWire[coord]
        wireIdAndSteps.update({wire_id: stepsTaken})
    else:
        wireIdAndSteps = {wire_id: stepsTaken}
        mapOfWire[coord] = wireIdAndSteps


def parseWire(wire):
    stepsTaken = 0
    x_coord = 0
    y_coord = 0
    actions = wire.split(",")
    for action in actions:
        act = splitAction(action)
        direction = act[0]
        steps = act[1]
        if direction == "R":  # Right
            # print("going right")
            startX = x_coord
            for _ in range(startX, startX + int(steps)):
                stepsTaken += 1
                x_coord += 1
                coord = (x_coord, y_coord)
                addOrUpdateMap(coord, wire_id, stepsTaken)

        if direction == "U":  # Up
            # print("going up")
            startY = y_coord
            for _ in range(startY, startY + int(steps)):
                stepsTaken += 1
                y_coord += 1
                coord = (x_coord, y_coord)
                addOrUpdateMap(coord, wire_id, stepsTaken)

        if direction == "L":  # Left
            # print("going left")
            startX = x_coord
            for _ in range(startX, x_coord - int(steps), -1):
                stepsTaken += 1
                x_coord -= 1
                coord = (x_coord, y_coord)
                addOrUpdateMap(coord, wire_id, stepsTaken)

        if direction == "D":  # Down
            # print("going down")
            startY = y_coord
            for _ in range(startY, y_coord - int(steps), -1):
                stepsTaken += 1
                y_coord -= 1
                coord = (x_coord, y_coord)
                addOrUpdateMap(coord, wire_id, stepsTaken)


for wire in input:
    wire = wire.strip("\n")
    parseWire(wire)
    wire_id += 1

intersectingCoordinates = set()
listOfSteps = []
for k, v in mapOfWire.items():
    if len(v) > 1:
        intersectingCoordinates.add(k)
        listOfSteps.append(v)

# print("intersecing coordinates" + str(intersectingCoordinates))
shortestManhattanDistance = np.inf
for point in intersectingCoordinates:
    mhd = calculateManhattanDistance(point)
    if mhd < shortestManhattanDistance:
        shortestManhattanDistance = mhd

print(f"the shortest manhattan distance is: {shortestManhattanDistance}")

# print(f"list of steps: {listOfSteps}")
fewestSteps = np.inf
for elems in listOfSteps:
    tmpSteps = elems[1] + elems[2]
    if tmpSteps < fewestSteps:
        fewestSteps = tmpSteps

print(f"fewest steps to collision is: {fewestSteps}")
