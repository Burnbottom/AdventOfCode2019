import math
from collections import defaultdict


def mySplit(s):
    name = s.lstrip("0123456789")  # striping the LEADING numbers
    amount = s[: len(s) - len(name)]
    return [amount, name]


def partA():
    file = open("init14.txt", "r")
    recepie = {}
    for row in file:
        break
    file.close()
