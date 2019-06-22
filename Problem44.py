def pentagon_nums_below(num):
    result = []
    n = 1
    while len(result) == 0 or result[-1] < num:
        result.append(n*(3*n-1)/2)
        n+=1
    return result


def find_min_diff_below(num):
    pens = pentagon_nums_below(num)
    min_d = None
    for i in range(len(pens)):
        for j in range(i, len(pens), 1):
            if (pens[j] - pens[i]) in pens:
                if (pens[j] + pens[i]) in pens:
                    if min_d is None or pens[j] - pens[i] < min_d:
                        min_d = pens[j] - pens[i]
    return min_d


print(find_min_diff_below(10000000))