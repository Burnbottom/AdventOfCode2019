def getLastVal(genIter):
    last = None
    for e in genIter:
        last = e
    return last


class Computer:
    def __init__(self, data):
        self.ptr = 0
        self.data = data[:]
        self.output = []
        self.done = False

    def getVal(self, val, mode):  # intermediate 1, position 0
        return val if mode else self.data[val]

    def add(self, param1, param2):
        return param1 + param2

    def multiply(self, param1, param2):
        return param1 * param2

    def run(self, input=None):
        while not self.done:
            instr = self.data[self.ptr]
            opCode = instr % 100
            modeFirst = instr // 100 % 10
            modeSecond = instr // 1000 % 10
            modeThird = instr // 10000 % 10

            # print(self.data)
            # print(f"prt: {self.ptr}, instr {instr}")
            if opCode == 99:
                self.done = True
            elif opCode == 1:  # addition
                pos = self.getVal(self.ptr + 3, modeThird)
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                arg2 = self.getVal(self.ptr + 2, modeSecond)
                self.data[pos] = self.add(self.data[arg1], self.data[arg2])
                self.ptr += 4
            elif opCode == 2:  # multiplication
                pos = self.getVal(self.ptr + 3, modeThird)
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                arg2 = self.getVal(self.ptr + 2, modeSecond)
                self.data[pos] = self.multiply(self.data[arg1], self.data[arg2])
                self.ptr += 4
            elif opCode == 3:  # insert
                pos = self.getVal(self.ptr + 1, modeFirst)
                self.data[pos] = input
                self.ptr += 2
            elif opCode == 4:  # output
                pos = self.getVal(self.ptr + 1, modeFirst)
                self.output.append(self.data[pos])
                # print(self.data)
                self.ptr += 2
                yield self.output
            elif opCode == 5:  # jump if true
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                if self.data[arg1] != 0:
                    arg2 = self.getVal(self.ptr + 2, modeSecond)
                    self.ptr = self.data[arg2]
                else:
                    self.ptr += 3
            elif opCode == 6:  # jump if false
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                if self.data[arg1] == 0:
                    arg2 = self.getVal(self.ptr + 2, modeSecond)
                    self.ptr = self.data[arg2]
                else:
                    self.ptr += 3
            elif opCode == 7:  # less than
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                arg2 = self.getVal(self.ptr + 2, modeSecond)
                pos = self.getVal(self.ptr + 3, modeThird)
                self.data[pos] = 1 if self.data[arg1] < self.data[arg2] else 0
                self.ptr += 4
            elif opCode == 8:  # equal to
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                arg2 = self.getVal(self.ptr + 2, modeSecond)
                pos = self.getVal(self.ptr + 3, modeThird)
                self.data[pos] = 1 if self.data[arg1] == self.data[arg2] else 0
                self.ptr += 4
            else:
                raise ValueError(f"Unknown opCode: {opCode}")
