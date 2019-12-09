class Computer:
    def __init__(self, data):
        self.ptr = 0
        self.data = data[:]
        self.done = False

    def getVal(self, val, mode):  # intermediate 1, position 0
        return val if mode else self.data[val]

    def add(self, param1, param2):
        return param1 + param2

    def multiply(self, param1, param2):
        return param1 * param2

    def run(self):
        while not self.done:
            instr = self.data[self.ptr]
            opCode = instr % 100
            modeFirst = instr // 100 % 10
            modeSecond = instr // 1000 % 10
            modeThird = instr // 10000 % 10

            if opCode == 99:
                self.done = True
                return self.data
            elif opCode == 1:
                arg1, arg2, pos = self.data[self.ptr + 1 : self.ptr + 4]

                self.data[pos] = self.add(
                    self.getVal(arg1, modeFirst), self.getVal(arg2, modeSecond)
                )
                self.ptr += 4
            elif opCode == 2:
                arg1, arg2, pos = self.data[self.ptr + 1 : self.ptr + 4]
                self.data[pos] = self.multiply(
                    self.getVal(arg1, modeFirst), self.getVal(arg2, modeSecond)
                )
                self.ptr += 4
            else:
                raise ValueError(f"Unknown opCode: {opCode}")
