import random

bile = []
sequence = []


def init(n, m, k):
    j = 0
    k2 = 0
    global bile
    global sequence
    bile = [None] * m * n
    for i in range(0, n * m):
        bile[i] = j
        k2 += 1
        if k2 == m:
            k2 = 0
            j += 1
    sequence = select(m, n, k)


def select(m, n, k):
    x = m * n
    alegere = random.sample(range(0, x - 1), k)
    return alegere


def check(seq):
    j = 0
    seq = [item for item in seq if item is not None]
    for i in seq:
        if i != bile[sequence[j]]:
            print("False")
            return False
        j += 1
    print("True")
    return True


# vect = select(2, 4, 3)
# print(vect)
init(4, 2, 6)
print(bile)
print(sequence)
seq = [None] * 8
seq[4] = 2
check(seq)
