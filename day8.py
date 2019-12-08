import numpy as np


def createLayer(dataSliced, heightLayer, widthLayer):
    tmp = [int(d) for d in dataSliced]
    oneDim = np.array(tmp)
    return oneDim.reshape(heightLayer, widthLayer)


def partA(inutData):
    numZeros = np.inf
    numOnes = 0
    numTwos = 0

    for elem in split:
        layer = createLayer(elem, height, width)
        tmpNumZeros = (layer == 0).sum()
        tmpNumOnes = (layer == 1).sum()
        tmpNumTwos = (layer == 2).sum()

        if tmpNumZeros < numZeros:
            numZeros = tmpNumZeros
            numOnes = tmpNumOnes
            numTwos = tmpNumTwos

    print(f"Part A : {numOnes*numTwos}")


def createLayerVector(inputData, height, width):
    layerList = np.zeros((len(inputData), height, width))
    layerid = 0
    for elem in split:
        layer = createLayer(elem, height, width)
        layerList[layerid] = layer
        layerid += 1

    return layerList


def decode(inputData, height, width):
    finalImage = np.zeros((height, width))
    for h in range(0, height):
        for w in range(0, width):
            for d in range(0, len(inputData)):
                tmpPointValue = inputData[d][h][w]
                if tmpPointValue != 2:
                    finalImage[h][w] = tmpPointValue
                    break

    return finalImage


# TestA
# input = "123456789012"
# width = 3
# height = 2

# Test B
# input = "0222112222120000"
# width = 2
# height = 2

file = open("init8.txt", "r")
input = file.readline()
file.close()
width = 25
height = 6

n = width * height
split = [input[i : i + n] for i in range(0, len(input), n)]

# partA(split)

layerList = createLayerVector(split, height, width)
finalImage = decode(layerList, height, width)
print(finalImage)
