def difference(n):
    sumsquare = 0
    squaresum = 0
    for i in range(1,n+1):
        sumsquare += (i**2)
        squaresum += i
    return squaresum**2 - sumsquare
