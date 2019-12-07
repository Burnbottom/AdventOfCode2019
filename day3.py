import numpy as np

input = open("data3.txt", "r")
mapOfWire = {}
wire_id = 1


def calculateManhattanDistance(intersectPoint):
    return abs(intersectPoint[0] - 0) + abs(intersectPoint[1] - 0)


def splitAction(action):
    return (action[0], action[1:])


def parseWire(wire):
    x_coord = 0
    y_coord = 0
    actions = wire.split(",")
    for action in actions:
        act = splitAction(action)
        direction = act[0]
        steps = act[1]
        # print("this is how many steps to walk " + steps)
        if direction == "R":  # Right
            # print("going right")
            startX = x_coord
            for _ in range(startX, startX + int(steps)):
                x_coord += 1
                coord = (x_coord, y_coord)
                if coord in mapOfWire:
                    # print("coordinate already existed: " + str(coord))
                    wires = mapOfWire[coord]
                    wires.add(wire_id)
                else:
                    # print("adding new coordinate: " + str(coord))
                    setOfWire = set([wire_id])
                    mapOfWire[coord] = setOfWire

        if direction == "U":  # Up
            # print("going up")
            startY = y_coord
            for _ in range(startY, startY + int(steps)):
                y_coord += 1
                coord = (x_coord, y_coord)
                if coord in mapOfWire:
                    # print("coordinate already existed: " + str(coord))
                    wires = mapOfWire[coord]
                    wires.add(wire_id)
                else:
                    # print("adding new coordinate: " + str(coord))
                    setOfWire = set([wire_id])
                    mapOfWire[coord] = setOfWire

        if direction == "L":  # Left
            # print("going left")
            startX = x_coord
            for _ in range(startX, x_coord - int(steps), -1):
                x_coord -= 1
                coord = (x_coord, y_coord)
                if coord in mapOfWire:
                    # print("coordinate already existed: " + str(coord))
                    wires = mapOfWire[coord]
                    wires.add(wire_id)
                else:
                    # print("adding new coordinate: " + str(coord))
                    setOfWire = set([wire_id])
                    mapOfWire[coord] = setOfWire

        if direction == "D":  # Down
            # print("going down")
            startY = y_coord
            for _ in range(startY, y_coord - int(steps), -1):
                y_coord -= 1
                coord = (x_coord, y_coord)
                if coord in mapOfWire:
                    # print("coordinate already existed: " + str(coord))
                    wires = mapOfWire[coord]
                    wires.add(wire_id)
                else:
                    # print("adding new coordinate: " + str(coord))
                    setOfWire = set([wire_id])
                    mapOfWire[coord] = setOfWire


for wire in input:
    wire = wire.strip("\n")
    # print("this is wire number: " + str(wire_id))
    parseWire(wire)
    wire_id += 1

intersectingCoordinates = set()
for k, v in mapOfWire.items():
    # print("coordinates: " + str(k) + " wires: " + str(v))
    if len(v) > 1:
        intersectingCoordinates.add(k)

# print("intersecing coordinates" + str(intersectingCoordinates))

nearestPoint = ()
shortestManhattanDistance = np.inf
for point in intersectingCoordinates:
    mhd = calculateManhattanDistance(point)
    if mhd < shortestManhattanDistance:
        shortestManhattanDistance = mhd

print("the shortest manhattan distance is: " + str(shortestManhattanDistance))
