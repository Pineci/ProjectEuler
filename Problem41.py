from functools import reduce
from math import sqrt

def pandigital(n):
    s = str(n)
    length = len(s)
    found = [False] * length
    if length >= 10:
        return False
    else:
        for i in s:
            index = int(i)-1
            if index >= length or index < 0:
                return False
            else:
                found[int(i)-1] = True
        return reduce(lambda x, y: x and y, found)

def primeSieve(max):
    primes = []
    primality = [True] * (max+1)
    primality[0] = False
    primality[1] = False
    for i in range(2, int(sqrt(max)) + 1):
        if primality[i]:
            for j in range(i*i, max+1, i):
                primality[j] = False
    for i in range(len(primality)):
        if primality[i]:
            primes.append(i)
    return primes

def largestPandigital():
    primes = primeSieve(100000000)
    for i in range(len(primes)-1, -1, -1):
        if pandigital(primes[i]):
            return primes[i]


print(largestPandigital())