import numpy as np
import math


def detectedAsteroids(station, listOfCandiates):
    detectedSet = set()
    for cand in listOfCandiates:
        if station != cand:
            dx, dy = cand[0] - station[0], cand[1] - station[1]
            gcd = abs(math.gcd(dx, dy))
            dist = (dx // gcd, dy // gcd)
            detectedSet.add(dist)
    return detectedSet


tmpList = []
data = open("input10.txt", "r")

for row in data:
    listData = [str(c) for c in row.strip()]
    tmpList.append(listData)

asteroids = np.array(tmpList)
result = np.where(asteroids == "#")
yPos = result[0]
xPos = result[1]
asteroidList = set()
for i in range(len(xPos)):
    asteroidList.add((xPos[i], yPos[i]))

stationCount = []
for station in asteroidList:
    los = detectedAsteroids(station, asteroidList)
    stationCount.append((len(los), station, los))
    # makes sure that the one with most asteroid in line of sight is at first position
    stationCount.sort(reverse=True)
    amtLos, station, los = stationCount[0]

print(f"Part 1: {amtLos}, at station {station}")
