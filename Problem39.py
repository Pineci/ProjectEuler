def numTriangles(perimeter):
    num = 0
    pSq = perimeter ** 2
    for a in range(1, perimeter):
        for b in range(a, perimeter):
            if pSq - 2*(a+b)*perimeter + 2*a*b == 0:
                num += 1

    return(num)

def maxNumTriangles(maxPerim):
    max = 0
    perim = 0
    for i in range(1, maxPerim+1):
        n = numTriangles(i)
        if n > max:
            perim = i
            max = n
    return perim


print(maxNumTriangles(1000))