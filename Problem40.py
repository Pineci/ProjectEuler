def concatenatedIntegers(maxLen):
    result = ""
    i = 1
    while len(result) < maxLen:
        result += str(i)
        i += 1
    return result

def champernowneConstant():
    expansion = concatenatedIntegers(1000000)
    prod = 1
    n = 1
    for i in range(7):
        prod *= int(expansion[n-1])
        n *= 10
    return prod

print(champernowneConstant())