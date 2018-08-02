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

def quadraticPrimeLength(a, b, primes):
    n = 0
    while n**2 + a*n + b in primes:
        n += 1
    return n

def findQuadratics(amax, bmax, primes):
    max = 0
    pair = [0, 0]
    bRange = list(filter(lambda x: x < bmax, primes))
    for a in range(1, amax, 2):
        for b in bRange:
            for sign in [[1, 1], [-1, 1], [1, -1], [-1, -1]]:
                qLen = quadraticPrimeLength(sign[0]*a, sign[1]*b, primes)
                if qLen > max:
                    max = qLen
                    pair = [sign[0]*a, sign[1]*b]
    return pair



primes = primeSieve(100000)
#bRange = list(filter(lambda x: x < 1000, primes))
#print(bRange)
pair = findQuadratics(1000, 1000, primes)
print(quadraticPrimeLength(pair[0], pair[1], primes))
print(pair)
print(pair[0] * pair[1])