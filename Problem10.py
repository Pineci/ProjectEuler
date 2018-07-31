from math import sqrt
import time

def primeSum(max):
    primeSum = 0
    primes = [True] * (max+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(sqrt(max))+1):
        if primes[i]:
            primeSum += i
            for j in range(i*i, max+1, i):
                primes[j] = False
    return primeSum

start = time.time()
print(primeSum(2000000))
print("Time Taken: " + str(time.time() - start))