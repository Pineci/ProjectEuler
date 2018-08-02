def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def factorialArray(start, end):
    result = []
    for i in range(start, end):
        result.append(factorial(i))
    return result

def curiousNumbers(max):
    factorials = factorialArray(0, 10)
    result = []
    for i in range(10, max):
        sumDigits = 0
        for s in str(i):
            sumDigits += factorials[int(s)]
        if sumDigits == i:
            result.append(i)
    return result

print(sum(curiousNumbers(1000000)))