sum = 0
limit = 4000000
series = [1,2]
while series[-1]<limit:
    if series[-1]%2 ==0:
        sum += series[-1]
    series.append(series[-1]+series[-2])
    
print(sum)
