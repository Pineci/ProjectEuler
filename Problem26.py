def findFirstIndexOf(element, list):
    for i in range(len(list)):
        if list[i] == element:
            return i

def reciprocalCycles(d):
    dividend = 1
    divisors = []
    remainders = [0]
    while remainders[-1] not in remainders[0:len(remainders)-1]:
        while dividend < d:
            divisors.append(0)
            dividend *= 10
        divisors.append(int(dividend/d))
        remainder = dividend % d
        remainders.append(remainder)
        dividend = remainder * 10
    if remainders[-1] == 0:
        return 0
    else:
        return len(remainders) - findFirstIndexOf(remainders[-1], remainders) - 1

def findMaxReciprocalCycles(limit):
    max = 0
    val = 2
    for i in range(2, limit):
        cycles = reciprocalCycles(i)
        if cycles > max:
            max = cycles
            val = i
    return val

print(reciprocalCycles(983))
print(findMaxReciprocalCycles(10000))