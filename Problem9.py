from functools import reduce

def pythagoreanTriple(m, n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return [a, b, c]


def findPythagoreanSum(x):
    i = 1
    j = 1
    triple = [0, 0, 0]
    while(sum(triple) != x):
        if (i == j):
            i += 1
            j = 1
        else:
            j += 1
        triple = pythagoreanTriple(i, j)
    return triple


print(reduce(lambda x, y: x*y, findPythagoreanSum(1000)))