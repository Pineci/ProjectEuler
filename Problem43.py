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

def numToArray(n):
    s = str(n)
    result = [0] * len(s)
    for i in range(len(s)):
        result[i] = int(s[i])
    return result

def substringDivisibility(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    s = str(n)
    for i in range(len(primes)):
        concat = int(s[i+1] + s[i+2] + s[i+3])
        print(concat)
        if concat % primes[i] != 0:
            return False
    print(n)
    return True

def pandigitalNumbers(min, max):
    s = ""
    for i in range(min, max+1):
        s += str(i)
    p = permutations(s)
    result = []
    for i in p:
        if int(i[0]) != 0 and i not in result:
            result.append(i)
    return list(map(lambda x: int(x), result))

pandigital = pandigitalNumbers(0, 9)
print(len(pandigital))
divisiblePandigital = list(filter(substringDivisibility,pandigital))
print(divisiblePandigital)
print(len(divisiblePandigital))
print(sum(divisiblePandigital))
