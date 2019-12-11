from computer import Computer
from itertools import permutations
from collections import deque


def amplifier(data, permutation):
    maxOutput = 0
    for phase in permutation:
        maxOutput = next(Computer(data.copy()).run(deque([phase, maxOutput])))
    return maxOutput


def feedback(data, permutation):
    done = False
    e_out = 0
    a_queue = deque([permutation[0], e_out])
    b_queue = deque([permutation[1]])
    c_queue = deque([permutation[2]])
    d_queue = deque([permutation[3]])
    e_queue = deque([permutation[4]])

    a = Computer(data.copy()).run(a_queue)
    b = Computer(data.copy()).run(b_queue)
    c = Computer(data.copy()).run(c_queue)
    d = Computer(data.copy()).run(d_queue)
    e = Computer(data.copy()).run(e_queue)

    while not done:
        b_queue.append(next(a, None))
        c_queue.append(next(b, None))
        d_queue.append(next(c, None))
        e_queue.append(next(d, None))

        try:
            e_out = next(e)
            a_queue.append(e_out)
        except:
            done = True
            break
    return e_out


data = "3,8,1001,8,10,8,105,1,0,0,21,30,47,60,81,102,183,264,345,426,99999,3,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,102,4,9,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99"
data = [int(d) for d in data.split(",")]

a = max(amplifier(data.copy(), permutation) for permutation in permutations(range(5)))
print(f"part A: {a}")


b = max(feedback(data, permutation) for permutation in permutations(range(5, 10)))

print(f"part B: {b}")  # 86129529 to low
