import math


def is_triangular(x):
    n = (math.sqrt(1+8*x)-1)/2
    return n.is_integer()


def is_pentagonal(x):
    n = (math.sqrt(1+24*x) + 1)/6
    return n.is_integer()


def find_all_three(num):
    n = 1
    hex = 1
    while hex < num:
        if is_pentagonal(hex) and is_triangular(hex):
            print(hex)
        n += 1
        hex = n*(2*n-1)

find_all_three(10000000000)