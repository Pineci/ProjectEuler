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

def truncatablePrime(x, primes):
    truncatable = True
    s = str(x)
    while truncatable and len(s) > 0:
        if int(s) not in primes:
            truncatable = False
        else:
            s = s[1:]
    s = str(x)
    while truncatable and len(s) > 0:
        if int(s) not in primes:
            truncatable = False
        else:
            s = s[:-1]
    return truncatable

primes = primeSieve(1000000)
truncatablePrimes = list(filter(lambda x: truncatablePrime(x, primes) and len(str(x)) > 1, primes))
print(truncatablePrimes)
print(len(truncatablePrimes))
print(sum(truncatablePrimes))