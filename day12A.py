import math

#  contains 3 lists, one for each axis
moonList = []
xPos = []
yPos = []
zPos = []
input = open("init12.txt", "r")
for row in input:
    row = row.strip("\n")
    row = row.replace(" ", "")
    row = row[1:-1]
    parts = row.split(",")
    xPos.append(parts[0][2:])
    yPos.append(parts[1][2:])
    zPos.append(parts[2][2:])
moonList.append(xPos)
moonList.append(yPos)
moonList.append(zPos)
input.close()


def runSim(positions, velocities, steps=float("inf")):
    origPos, origVel = positions[:], velocities[:]
    numSteps = 0
    while numSteps < steps and (
        not numSteps or positions != origPos or velocities != origVel
    ):
        for i in range(len(positions)):
            velocities[i] += sum(
                1 if positions[i] < position else -1
                for position in positions
                if position != positions[i]
            )

        for i in range(len(positions)):
            positions[i] += velocities[i]
        numSteps += 1
    return numSteps


def part1(positions):
    px, vx = [int(x) for x in positions[0]], [0] * len(positions[0])
    py, vy = [int(y) for y in positions[1]], [0] * len(positions[0])
    pz, vz = [int(z) for z in positions[2]], [0] * len(positions[0])

    for p, v in zip((px, py, pz), (vx, vy, vz)):
        runSim(p, v, 1000)

    return sum(
        (abs(px[i]) + abs(py[i]) + abs(pz[i])) * (abs(vx[i]) + abs(vy[i]) + abs(vz[i]))
        for i in range(len(positions[0]))
    )


def lcm(a, b):
    return a * b // math.gcd(a, b)


def part2(positions):
    px, vx = [int(x) for x in positions[0]], [0] * len(positions[0])
    py, vy = [int(y) for y in positions[1]], [0] * len(positions[0])
    pz, vz = [int(z) for z in positions[2]], [0] * len(positions[0])

    stepsX = runSim(px, vx)
    stepsY = runSim(py, vy)
    stepsZ = runSim(pz, vz)

    return lcm(lcm(stepsX, stepsY), stepsZ)


print(f"Part A : {part1(moonList)}, Part B: {part2(moonList)}")
