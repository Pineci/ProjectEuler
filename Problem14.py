def nextCollatzTerm(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1

def collatzSequence(n):
    seq = [n]
    c = nextCollatzTerm(n)
    while seq[-1] != 1:
        seq.append(c)
        c = nextCollatzTerm(c)
    return seq

lengths = list(map(lambda x: len(collatzSequence(x)), list(range(1, 1000000))))
max = 0
maxSeed = 0
for i in range(len(lengths)):
    if lengths[i] > max:
        max = lengths[i]
        maxSeed = i+1
print(maxSeed)