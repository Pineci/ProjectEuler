from functools import reduce
from math import sqrt

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

def circular(num):
    s = str(num)
    result = [s]
    for i in range(len(s)-1):
        last = result[-1]
        result.append(last[-1] + last[:-1])
    return list(map(int, result))

def circularPrime(num, primes):
    return reduce(lambda x, y: x and y, list(map(lambda x: x in primes, circular(num))))

def noEvenDigits(num):
    res = True
    for i in str(num):
        if int(i) % 2 == 0:
            res = False
    return res

n = 1000000
primes = primeSieve(n)
l = list(filter(lambda x: circularPrime(x, primes), list(filter(noEvenDigits, primes))))
print(l)
print(len(l)+1)