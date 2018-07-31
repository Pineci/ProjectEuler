from functools import reduce

def union(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result

def primeSieve(max):
    primes = []
    multiples = []
    for i in range(2, max+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, max+1, i):
                multiples.append(j)
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

def divisibleBy(max):
    primes = primeSieve(max)
    return reduce(lambda x, y: x*y, reduce(union, map(lambda x: factorize(x, primes), list(range(2, max+1)))))

print(divisibleBy(20))
