from collections import defaultdict


def getLastVal(genIter):
    last = None
    for e in genIter:
        last = e
    return last


class Computer:
    def __init__(self, data):
        self.ptr = 0
        self.data = defaultdict(int, enumerate(data))
        self.output = []
        self.base = 0

    def getInd(self, index, mode):  # relative 2 intermediate 1, position 0
        if mode == 0:
            return self.data[index]
        elif mode == 1:
            return index
        elif mode == 2:
            return self.data[index] + self.base
        else:
            raise ValueError(f"Unknown mode: {mode}")

    def getVal(self, val, mode):
        tmp = self.getInd(val, mode)
        return self.data[tmp]

    def add(self, param1, param2):
        return param1 + param2

    def multiply(self, param1, param2):
        return param1 * param2

    def run(self, input_queue=None):
        while True:
            instr = self.data[self.ptr]
            opCode = instr % 100
            modeFirst = instr // 100 % 10
            modeSecond = instr // 1000 % 10
            modeThird = instr // 10000 % 10

            #print(self.data)
            #print(self.output)
            #print(f"prt: {self.ptr}, instr {instr}, rel ptr: {self.base}")
            if opCode == 99:
                break
            elif opCode == 1:  # addition
                pos = self.getInd(self.ptr + 3, modeThird)
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                arg2 = self.getVal(self.ptr + 2, modeSecond)
                self.data[pos] = self.add(arg1, arg2)
                self.ptr += 4
            elif opCode == 2:  # multiplication
                pos = self.getInd(self.ptr + 3, modeThird)
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                arg2 = self.getVal(self.ptr + 2, modeSecond)
                self.data[pos] = self.multiply(arg1, arg2)
                self.ptr += 4
            elif opCode == 3:  # insert
                pos = self.getInd(self.ptr + 1, modeFirst)
                if pos < 0:
                    raise IndexError("Tried to read out of memory")
                self.data[pos] = input_queue #input_queue.popleft()
                self.ptr += 2
            elif opCode == 4:  # output
                pos = self.getInd(self.ptr + 1, modeFirst)
                if pos < 0:
                    raise IndexError("Tried to read out of memory")
                self.output.append(self.data[pos])
                print(self.output[-1])
                self.ptr += 2
                #yield self.output[-1]
                #self.ptr += 2
            elif opCode == 5:  # jump if true
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                if arg1 != 0:
                    arg2 = self.getVal(self.ptr + 2, modeSecond)
                    self.ptr = arg2
                else:
                    self.ptr += 3
            elif opCode == 6:  # jump if false
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                if arg1 == 0:
                    arg2 = self.getVal(self.ptr + 2, modeSecond)
                    self.ptr = arg2
                else:
                    self.ptr += 3
            elif opCode == 7:  # less than
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                arg2 = self.getVal(self.ptr + 2, modeSecond)
                pos = self.getInd(self.ptr + 3, modeThird)
                self.data[pos] = 1 if arg1 < arg2 else 0
                self.ptr += 4
            elif opCode == 8:  # equal to
                arg1 = self.getVal(self.ptr + 1, modeFirst)
                arg2 = self.getVal(self.ptr + 2, modeSecond)
                pos = self.getInd(self.ptr + 3, modeThird)
                self.data[pos] = 1 if arg1 == arg2 else 0
                self.ptr += 4
            elif opCode == 9:
                self.base += self.getVal(self.ptr + 1, modeFirst)
                self.ptr += 2
            else:
                raise ValueError(f"Unknown opCode: {opCode}")
