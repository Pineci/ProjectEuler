from functools import reduce

def gcd(x, y):
    a = max(x, y)
    b = min(x, y)
    r = a
    while r > 0:
        r = a % b
        a = b
        b = r
    return a

def twoDigitPairsNoZeroes():
    pairs = []
    for i in range(11, 100):
        for j in range(i+1, 100):
            if '0' not in str(i) and '0' not in str(j):
                pairs.append([i, j])
    return pairs

def cancelDigitDuplciates(x):
    a = str(x[0])
    b = str(x[1])
    result = [x[0], x[1]]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result[0] = int(a[len(a)-1-i])
                result[1] = int(b[len(b)-1-j])
                return result

class fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        #print(self)
        d = gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / d)
        self.denominator = int(self.denominator / d)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __mul__(self, f):
        new = fraction(self.numerator * f.numerator, self.denominator * f.denominator)
        new.simplify()
        return new

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

def cancellingFraction(x):
    f = fraction(x[0], x[1])
    cancel = cancelDigitDuplciates(x)
    if cancel is not None:
        c = fraction(cancel[0], cancel[1])
        f.simplify()
        c.simplify()
        return f == c
    else:
        return False

fracPairs = list(filter(cancellingFraction, twoDigitPairsNoZeroes()))
fracs = []
for f in fracPairs:
    fracs.append(fraction(f[0], f[1]))
prod = reduce(lambda x, y: x*y, fracs)
prod.simplify()
print(prod)


