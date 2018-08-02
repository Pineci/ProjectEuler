def palindrome(s):
    return s == s[::-1]


def changeBase(n, base):
    numDigits = 0
    while base ** numDigits <= n:
        numDigits += 1
    remainder = n
    number = []
    for i in range(numDigits-1, -1, -1):
        digit = base ** i
        quotient = int(remainder/digit)
        number.append(quotient)
        remainder = remainder % digit
    return number


def palindromesLessThan(max):
    results = []
    for i in range(max):
        if palindrome(str(i)):
            results.append(i)
    return results


def doubleBasePalindromes(max):
    baseTenPalindromes = palindromesLessThan(max)
    results = []
    for i in baseTenPalindromes:
        if palindrome(changeBase(i, 2)):
            results.append(i)
    return results


palindromes = doubleBasePalindromes(1000000)
print(palindromes)
print(sum(palindromes))
