
def no_duplicates(*args):
    list = []
    for arg in args:
        list.append(arg)
    return len(list) == len(set(list))

def pandigital_sum_candidates():
    results = []
    evens = ["0", "2", "4", "6", "8"]
    standard = ["0", "1", "2", "3", "4", "6", "7", "8", "9"]
    d6 = "5"
    for d1 in ["1", "2", "3", "4", "6", "7", "8", "9"]:
        for d2 in standard:
            if no_duplicates(d1, d2):
                for d3 in standard:
                    if no_duplicates(d1, d2, d3):
                        for d4 in evens:
                            if no_duplicates(d1, d2, d3, d4):
                                for d5 in standard:
                                    if no_duplicates(d1,d2,d3,d4,d5) and int(d3+d4+d5) % 3 == 0:
                                        if d1+d2+d3+d4+d5 == "14063":
                                            print("made it")
                                        for d7 in standard:
                                            if d7 != "4" and no_duplicates(d1, d2, d3,d4,d5,d7) and int(d5+d6+d7) % 7 == 0:
                                                if d1 + d2 + d3 + d4 + d5 == "14063":
                                                    print("made it twice")
                                                d8 = 0
                                                if(int(d7) < 5):
                                                    d8 = str(int(d7) + 6)
                                                else:
                                                    d8 = str(int(d7)-5)
                                                if no_duplicates(d1,d2,d3,d4,d5,d7,d8):
                                                    if d1 + d2 + d3 + d4 + d5 == "14063":
                                                        print("made it thrice")
                                                        print(d1+d2+d3+d4+d5+d6+d7+d8)
                                                    for d9 in standard:
                                                        if no_duplicates(d1,d2,d3,d4,d5,d7,d8,d9) and int(d7+d8+d9) % 13 == 0:

                                                            for d10 in standard:
                                                                if no_duplicates(d1,d2,d3,d4,d5,d7,d8,d9,d10) and int(d8+d9+d10) % 17 == 0:
                                                                    results.append(int(d1+d2+d3+d4+d5+d6+d7+d8+d9+d10))
    return results

#print(no_duplicates("1", "2", "3"))
#print(no_duplicates("1", "2", "1"))

print(sum(pandigital_sum_candidates()))