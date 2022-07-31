def powerdigitsum(n,p):
    sum = 0
    for i in str(n**p):
        sum += int(i)
    return sum

print(powerdigitsum(2,1000))
