
def spiralDiagonal(maxDim):
    diagonals = [1]
    n = 2
    while n <= maxDim-1:
        last = diagonals[-1]
        if last >= (n+1)**2:
            n+=2
        else:
            diagonals.append(last+n)
    return diagonals

print(sum(spiralDiagonal(1001)))