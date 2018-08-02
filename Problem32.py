from functools import reduce

def permutations(str):
    if len(str) == 1:
        return str
    else:
        results = []
        for i in range(len(str)):
            start = str[i]
            p = permutations(str.replace(start, ""))
            results = results + list(map(lambda x: start + x, p))
        return results

def pandigitalProduct(pan):
    products = []
    length = len(pan)
    for i in range(length-2):
        for j in range(i, length-2):
            multiplicand = int(pan[0:i+1])
            multiplier = int(pan[i+1:j+2])
            prod = multiplicand * multiplier
            if prod == int(pan[j+2:length]):
                products.append(prod)
    return products

def union(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result

panProds = reduce(union, list(map(pandigitalProduct, permutations("123456789"))))
print(sum(panProds))
#print(pandigitalProduct("391867254"))
#print(permutations("123456789"))