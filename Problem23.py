from math import sqrt
from functools import reduce

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

def divisors(x, primes):
    factors = factorizeWithPowers(x, primes)
    divisors = []
    powers = [0] * len(factors)
    numDivisors = 1
    for i in range(len(factors)):
        numDivisors *= (factors[i][1]+1)
    for i in range(numDivisors):
        val = 1
        carry = True
        for j in range(len(factors)):
            val *= factors[j][0] ** powers[j]
            if carry:
                if powers[j] == factors[j][1]:
                    powers[j] = 0
                else:
                    powers[j] += 1
                    carry = False
        divisors.append(val)
    return divisors

def properDivisorSum(x, primes):
    if x == 1:
        return 1
    else:
        d = divisors(x, primes)
        del d[-1]
        return reduce(lambda x, y: x+y, d)

def abundant(x, primes):
    return properDivisorSum(x, primes) > x

def notSumOfTwoAbundantNumber(max, primes):
    resultBooleans = [True] * max
    result = []
    abundantNumbers = []
    for i in range(1, max+1):
        if abundant(i, primes):
            abundantNumbers.append(i)
    print(abundantNumbers)
    #print(list(filter(lambda x : x % 2 == 1, abundantNumbers)))
    for i in range(len(abundantNumbers)):
        for j in range(i, len(abundantNumbers)):
            sum = abundantNumbers[i] + abundantNumbers[j]
            if sum <= len(resultBooleans):
                resultBooleans[sum-1] = False
    for i in range(len(resultBooleans)):
        if resultBooleans[i]:
            result.append(i+1)
    return result







primes = primeSieve(100000)
n = 28123
l = notSumOfTwoAbundantNumber(n, primes)
print(l)
print(list(filter(lambda x: x not in l, list(range(1, n)))))
print(sum(l))