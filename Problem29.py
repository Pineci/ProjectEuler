
def powers(aMax, bMax):
    a = 2
    b = 2
    results = []
    while a <= aMax:
        while b <= bMax:
            results.append(a ** b)
            b += 1
        b = 2
        a += 1
    return results

def distinct(list):
    newList = []
    for i in range(len(list)):
        l = list[i]
        if l not in newList:
            newList.append(l)
    return newList

print(len(distinct(powers(100, 100))))