def palindrome(x):
    s = str(x)
    l = len(s)
    a = s[0:int(l/2)]
    b = s[int(l/2) + l%2:l]
    return a == b[::-1]

def productsCombination(start, stop):
    result = []
    for i in range(start, stop):
        for j in range(start, stop):
            result.append(i*j)
    return result

print(max(list(filter(palindrome, productsCombination(100, 1000)))))