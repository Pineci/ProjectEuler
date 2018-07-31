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


def multiples(x, max):
    result = []
    val = x
    while val < max:
        result.append(val)
        val += x
    return result

x = multiples(3, 1000)
y = multiples(5, 1000)
print(sum(union(x, y)))
