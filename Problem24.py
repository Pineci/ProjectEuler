
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

print(permutations("0123456789")[1000000-1])
