
def addDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum


print(addDigits(2**1000))