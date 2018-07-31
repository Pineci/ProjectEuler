def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def sumDigits(n):
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum

print(sumDigits(factorial(100)))