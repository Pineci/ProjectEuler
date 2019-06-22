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


def powers_below(max_num):
    powers = []
    n = 1
    p = n ** 2
    while p < max_num:
        powers.append(p)
        n += 1
        p = n ** 2
    return powers


#'@param Max Num is the largest possible input,
# must have max_num > 8
def non_goldbach_composites_below(max_num):
    powers = powers_below(max_num)
    primes = prime_sieve(max_num)
    goldbachs = [False] * (max_num + 1)
    for p in primes:
        for n in powers:
            a = p + 2*n
            if a < max_num:
                goldbachs[a] = True
    odd_composites = filter(lambda x: x not in primes and x % 2 == 1, range(8, max_num, 1))
    for x in odd_composites:
        if not goldbachs[x]:
            print(x)


non_goldbach_composites_below(10000)

#max_num  = 1000
#primes = prime_sieve(max_num)
#composites = list(filter(lambda x: x not in primes and x % 2 == 1, range(8, max_num, 1)))
#print(composites)