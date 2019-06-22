from math import sqrt
from functools import reduce


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


def consecutive_prime_sum_below(max_num, primes):
    longest_sum = [0] * (max_num+1)
    done = False
    terms = 2
    while not done:
        consecutive_primes = []
        for i in range(len(primes) - terms):
            consecutive_primes.append(primes[i:i+terms])
        consecutive_sums = list(map(lambda l: reduce(lambda x,y: x+y, l), consecutive_primes))
        for i in range(len(consecutive_sums)):
            num = consecutive_sums[i]
            if i == 0 and num > max_num:
                done = True
            if num <= max_num:
                longest_sum[num] = terms
            else:
                break
        terms += 1
        print("Terms: " + str(terms) + " First Sum: " + str(consecutive_sums[0]) + " Last Sum: " + str(consecutive_sums[-1]))
        if terms > len(primes):
            done = True
    return longest_sum

def print_longest_sums(max_num):
    primes = prime_sieve(max_num)
    longest_sums = consecutive_prime_sum_below(max_num, primes)
    max_terms = 0
    max_num = 0
    for i in range(len(longest_sums)):
        if longest_sums[i] > max_terms and i in primes:
            max_terms = longest_sums[i]
            max_num = i
    print(str(max_num) + " " + str(max_terms))

print_longest_sums(1000000)

