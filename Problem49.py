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


def choose_list_internal(l, n):
    if n == 1:
        return list(map(lambda x: tuple([x]), l))
    elif n == len(l):
        return [tuple(l)]
    elif n < len(l):
        result_unsorted = []
        result = []
        for i in range(len(l)):
            element = l[i]
            remaining_combos = choose_list_internal(l[0:i] + l[i+1:], n-1)
            for combo in remaining_combos:
                result_unsorted.append(tuple([element]) + combo)
        for alon in result_unsorted:
            result.append(tuple(sorted(alon)))
        return set(result)

def choose_list(l, n):
    if n == 0:
        return None
    else:
        return list(map(list, list(choose_list_internal(l, n))))


def permute_list(l):
    if len(l) == 1:
        return l
    else:
        result = []
        for i in range(len(l)):
            for element in permute_list(l[0:i] + l[i + 1:]):
                result.append(l[i] + element)
        return result


def permute_string(s):
    return list(map(str, permute_list(list(s))))


def permute_int(x):
    return list(map(int, permute_string(str(x))))
            

def four_digit_prime_permutations():
    four_digits = list(filter(lambda x: x >= 1000, prime_sieve(10000)))
    result = []
    while len(four_digits) > 0:
        p = four_digits[0]
        four_digits.remove(p)
        permutations = permute_int(p)
        prime_permutations = []
        for perm in permutations:
            if perm in four_digits:
                prime_permutations.append(perm)
                four_digits.remove(perm)
        if len(prime_permutations) > 0:
            prime_permutations.append(p)
            prime_permutations.sort()
            result.append(prime_permutations)
    return result


def is_arithmetic_sequence(seq):
    result = False
    if len(seq) > 2:
        result = True
        d = seq[1] - seq[0]
        for i in range(1, len(seq)-1, 1):
            next_d = seq[i+1] - seq[i]
            if d != next_d:
                result = False
    return result

print(choose_list([1,2,3,4], 4))
#possible_arithmetic_sequences = four_digit_prime_permutations()
#print(is_arithmetic_sequence(possible_arithmetic_sequences[0]))
print(list(filter(is_arithmetic_sequence, reduce(lambda x,y: x + y, map(lambda l: choose_list(l, 3), filter(lambda l: len(l) >= 3, four_digit_prime_permutations()))))))