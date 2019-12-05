numbers = []

for i in range(359282, 820401):
    numbers.append(str(i))

increasing = []
for elem in numbers:
    if list(elem) == sorted(elem):
        increasing.append(elem)

okNeigbour = []
for num in increasing:
    for digit in num:
        count = num.count(digit)
        if count == 2:
            okNeigbour.append(num)
            break

print(len(okNeigbour))
