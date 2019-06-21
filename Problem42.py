import re

def readWords():
    with open('Problem42Words.txt') as f:
        raw = f.read()
    words = raw.split(',')
    for i in range(len(words)):
        words[i] = re.sub('"', '', words[i])
    return words



def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivotIndex = int(len(list) / 2)
        pivot = list[pivotIndex]
        below = []
        above = []
        for i in range(len(list)):
            if i != pivotIndex:
                if list[i] < pivot:
                    below.append(list[i])
                else:
                    above.append(list[i])
        return quickSort(below) + [pivot] + quickSort(above)

def letterToNumber(letter):
    return ord(letter) - 64

def stringToNumber(string):
    return sum(map(letterToNumber, string))

def triangleNumbers(maxLength):
    result = [0] * maxLength
    for i in range(1, maxLength+1):
        result[i-1] = int(0.5 * i * (i+1))
    return result


words = readWords()
triangles = triangleNumbers(100)
triangleWords = list(filter(lambda x: stringToNumber(x) in triangles, words))
print(triangleWords)
print(len(triangleWords))