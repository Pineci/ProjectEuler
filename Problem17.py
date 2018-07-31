from functools import reduce

class NumberWords():

    def __init__(self, n):
        self.n = n

    def SetN(self, n):
        self.n = n

    def word(self, s):
        if len(s) < 3:
            return self.wordTens(s)
        else:
            return self.wordHundreds(s)

    def wordHundreds(self, s):
        a = s[0]
        b = s[1:3]
        connector = " and "
        if b == "00":
            connector = ""
        return self.wordTens(a) + " hundred" + connector + self.wordTens(b)

    def wordTens(self, s):
        if s == "0":
            return "zero"
        if s == "1" or s == "01":
            return "one"
        if s == "2" or s == "02":
            return "two"
        if s == "3" or s == "03":
            return "three"
        if s == "4" or s == "04":
            return "four"
        if s == "5" or s == "05":
            return "five"
        if s == "6" or s == "06":
            return "six"
        if s == "7" or s == "07":
            return "seven"
        if s == "8" or s == "08":
            return "eight"
        if s == "9" or s == "09":
            return "nine"
        if s == "10":
            return "ten"
        if s == "11":
            return "eleven"
        if s == "12":
            return "twelve"
        if s == "13":
            return "thirteen"
        if s == "14":
            return "fourteen"
        if s == "15":
            return "fifteen"
        if s == "16":
            return "sixteen"
        if s == "17":
            return "seventeen"
        if s == "18":
            return "eighteen"
        if s == "19":
            return "nineteen"
        if s == "00":
            return ""
        else:
            a = s[0]
            b = s[1]
            units = self.wordTens(b)
            if b == "0":
                units = ""
            return self.wordTensPrefix(a) + " " + units

    def wordTensPrefix(self, s):
        if s == "2":
            return "twenty"
        if s == "3":
            return "thirty"
        if s == "4":
            return "forty"
        if s == "5":
            return "fifty"
        if s == "6":
            return "sixty"
        if s == "7":
            return "seventy"
        if s == "8":
            return "eighty"
        if s == "9":
            return "ninety"
        else:
            raise ValueError("Was not given an input within the right domain [2, 9] for the prefixes of the first hundred numbers!")



w = NumberWords(1)
print(len(list(filter(lambda x: x != " ", list(w.word("115"))))))
print(list(map(lambda x: ''.join(list(filter(lambda x: x != " ", list(w.word(str(x)))))), list(range(1, 1000)))))
print(list(map(lambda x: len(list(filter(lambda x: x != " ", list(w.word(str(x)))))), list(range(1, 1000)))))
total = reduce(lambda x, y: x + y, list(map(lambda x: len(list(filter(lambda x: x != " ", list(w.word(str(x)))))), list(range(1, 1000)))))
total += len("onethousand")
print(total)