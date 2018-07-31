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

def factorize(x, primes):
    factors = []
    val = x
    i = 0
    while i < len(primes):
        if val % primes[i] == 0:
            factors.append(primes[i])
            val /= primes[i]
        else:
            i += 1
    assert val == 1, "Not enough primes given! Remaining value: " + str(val)
    return factors

def factorizeWithPowers(x, primes):
    factors = factorize(x, primes)
    result = []
    base = primes[0]
    power = 0
    for i in range(len(factors)):
        if factors[i] == base:
            power += 1
        else:
            result.append([base, power])
            base = factors[i]
            power = 1
    result.append([base, power])
    return result

def numDivisors(x, primes):
    factors = factorizeWithPowers(x, primes)
    numDivisors = 1
    for i in range(len(factors)):
        numDivisors *= (factors[i][1]+1)
    return numDivisors

def triangularNumber(n):
    return int(n*(n+1)/2)

def triangleGreatestNumDivisors(max, primes):
    greatestDivisors = 0
    n = 1
    while max > greatestDivisors:
        divisors = numDivisors(triangularNumber(n), primes)
        if greatestDivisors < divisors:
            greatestDivisors = divisors
        n += 1
    return triangularNumber(n-1)




primes = primeSieve(100000)
print(triangleGreatestNumDivisors(500, primes))