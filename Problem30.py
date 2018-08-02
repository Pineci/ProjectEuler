def digitPowers(n, p):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i) ** p
    return sum

def digitPowersSum(max, p):
    results = []
    for i in range(2, max):
        if digitPowers(i, p) == i:
            results.append(i)
    return results

digitSums = digitPowersSum(1000000, 5)
print(sum(digitSums))
print(digitSums)
