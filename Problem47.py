from math import sqrt

def prime_sieve(max_num):
    primes = []
    primality = [True] * (max_num+1)
    primality[0] = False
    primality[1] = False
    for i in range(2, int(sqrt(max_num)) + 1):
        if primality[i]:
            for j in range(i*i, max_num+1, i):
                primality[j] = False
    for i in range(len(primality)):
        if primality[i]:
            primes.append(i)
    return primes


def find_factors(num, primes, factors):
    if num in factors:
        return factors[num]
    else:
        if num in primes:
            return [num]
        else:
            for p in primes:
                factor = float(num) / float(p)
                if factor.is_integer():
                    return find_factors(int(factor), primes, factors) + [p]




def prime_factors(max_num):
    factors = {}
    primes = prime_sieve(max_num)
    for x in range(2, max_num, 1):
        f = find_factors(x, primes, factors)
        f.sort()
        factors[x] = f
    return factors


def n_consecutive_distinct_factors(n, max_num):
    factors = prime_factors(max_num)
    for i in range(2, max_num-n+1, 1):
        distinct = True
        for j in range(0, n-1, 1):
            set1 = set(factors[i+j])
            set2 = set(factors[i+j+1])
            setU = set(factors[i+j] + factors[i+j+1])
            if not (len(set1) >= n and len(set2) >= n and len(set1) + len(set2) == len(setU)):
                distinct = False
        if distinct:
            return i

#print(list(range(0, 5, 1)))
print(n_consecutive_distinct_factors(4, 1000000))



