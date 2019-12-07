import numpy as np

planets = dict()
planets["COM"] = None
for line in open("init6.txt", "r"):
    line = line.strip("\n")
    split = line.split(")")
    planets[split[1]] = split[0]

count = 0
for key in planets.keys():
    tmp = planets[key]
    while True:
        if tmp == None:
            break
        else:
            count += 1
            tmp = planets[tmp]
print(f"Part A: {count}")

tmp = planets[planets["YOU"]]
youWalking = {}
countYOU = 0
while True:
    if tmp == None:
        break
    else:
        countYOU += 1
        youWalking[tmp] = countYOU
        tmp = planets[tmp]

tmp = planets[planets["SAN"]]
countSAN = 0
while True:
    if tmp == None:
        break
    else:
        countSAN += 1
        if tmp in youWalking:
            print(f"orbital transfer required : {countSAN + youWalking[tmp]}")  # 304
            break
        tmp = planets[tmp]
