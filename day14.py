import math
from collections import defaultdict


def mySplit(s):
    name = s.lstrip("0123456789")  # striping the LEADING numbers
    amount = s[: len(s) - len(name)]
    return [amount, name]


def findIngredients(recepie):
    ingredients = {}
    for ingred in recepie.values():
        for key in ingred:
            if key not in ingredients:
                ingredients[key] = ingred[key]
            else:
                ingredients[key] += ingred[key]
    return ingredients


def findBasicElement(recepie):
    basicElements = {}
    for key, value in recepie.items():
        for key2 in value:
            if key2 == "ORE":
                basicElements[key[0]] = (int(key[1]), value[key2])

    return basicElements


def calcOre(allElem, basicElem):
    totOre = 0
    for basic in basicElem:
        multiplier = math.ceil(int(allElem[basic]) / int(basicElem[basic][0]))
        totOre += multiplier * int(basicElem[basic][1])
    return totOre


def findFuelReq(recepie):
    tmp = {}
    for keyList in recepie:
        if "FUEL" in keyList:
            for req in recepie[keyList]:
                tmp[req] = int(keyList[1]) * int(recepie[keyList][req])
    return tmp


# X AB need Y A and Z B etc
def breakDown(recepie, allIngredients, basicElem):
    print(allIngredients)
    for keyList in recepie:
        for key in allIngredients:
            if key not in basicElem.keys() and not key == "ORE":
                tmpMap = defaultdict(int)
                print(allIngredients[key])
    # return output


file = open("init14.txt", "r")
recepie = {}
for row in file:
    ingredients = {}
    row = row.strip("\n")
    row = row.replace(" ", "")
    arrow = row.find("=>")
    ind = row[:arrow]
    output = row[arrow + 2 :]
    for part in ind.split(","):
        splitString = mySplit(part)
        ingredients[splitString[1]] = int(splitString[0])
    outSplit = mySplit(output)

    recepie[(outSplit[1], outSplit[0])] = ingredients


allIngredients = findIngredients(recepie)
basicElem = findBasicElement(recepie)
fuelReq = findFuelReq(recepie)

breakDown(recepie, allIngredients, basicElem)
# print("Part A", calcOre(brokenDown, basicElem))
