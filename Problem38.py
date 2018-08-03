from functools import reduce

def concatenatedProduct(n, maxDigits):
    i = 1
    concatProd = ""
    while len(concatProd) < maxDigits:
        concatProd += str(i*n)
        i += 1
    return int(concatProd)

def pandigital(n):
    found = [False] * 9
    s = str(n)
    for i in s:
        found[int(i)-1] = True
    return reduce(lambda x, y: x and y, found)


def pandigitalMultiples(max):
    multiples = []
    for i in range(1, max):
        prod = concatenatedProduct(i, 9)
        if len(str(prod)) == 9 and pandigital(prod):
            multiples.append(prod)
    return multiples


print(max(pandigitalMultiples(1000000)))