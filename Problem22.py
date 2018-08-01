import re

def readNames():
    with open('Problem22Names.txt') as f:
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

def nameScores(list):
    scores = []
    for i in range(len(list)):
        scores.append((i+1)*stringToNumber(list[i]))
    return scores




names = readNames()
sortedNames = quickSort(names)
scores = nameScores(sortedNames)
print(sum(scores))