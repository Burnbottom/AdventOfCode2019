import math

input = open("data01.txt", "r")


def calc_fuel(data):
    # divide by 3, round down, subtract 2
    return math.floor(int(data) / 3) - 2


total_fuel = 0
for e in input:
    done = False
    module_fuel = 0
    tmp = e
    while not done:
        tmp = calc_fuel(tmp)
        if tmp < 0:
            total_fuel += module_fuel
            done = True
        else:
            module_fuel += tmp

print("total fuel needed: " + str(int(total_fuel)))
