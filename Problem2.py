def fibonacci(max):
    fib = [1, 1]
    i = 1
    while(fib[i] < max):
        fib.append(fib[i] + fib[i-1])
        i += 1
    return fib[0:i]

#print(fibonacci(4e6))
#print(list(filter(lambda x: x % 2 != 0, fibonacci(4e6))))
print(sum(list(filter(lambda x: x % 2 != 0, fibonacci(4e6)))))