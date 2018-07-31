from math import log

def primeSieve(count):
    primes = []
    multiples = []
    i = 2
    max = int((count+1)*(log(count+1) + log(log(count+1))))
    while len(primes) < count:
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, max+1, i):
                if j not in multiples:
                    multiples.append(j)
        i += 1
    return primes

def prime(n):
    return primeSieve(n)[-1]

print(prime(10001))