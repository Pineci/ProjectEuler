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

#print(primeSieve(100))
primes = primeSieve(10000)
print(primes)
print(len(primes))
print(factorize(600851475143, primes))