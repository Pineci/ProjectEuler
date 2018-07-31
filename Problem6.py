def sumSquareDifference(max):
    l = list(range(1, max+1))
    return sum(l)**2 - sum(map(lambda x: x*x, l))

print(sumSquareDifference(100))