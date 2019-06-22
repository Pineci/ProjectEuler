

def pow_sum(max, mod):
    acc = 0
    for i in range(1, max+1, 1):
        acc += pow(i, i, mod)
    return acc % mod

print(pow_sum(1000, 10000000000))