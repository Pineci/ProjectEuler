
def FibonacciDigits(max):
    a = 1
    b = 1
    index = 2
    while(len(str(b)) < max):
        temp = a+b
        a = b
        b = temp
        index+=1
    return index

print(FibonacciDigits(1000))