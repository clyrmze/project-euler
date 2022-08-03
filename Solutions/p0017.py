single = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
6:'six',7:'seven',8:'eight',9:'nine'}

double = {
    11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',
    15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'
}

triple = {1000:'one thousand'}

Zeros = {
    10:'ten',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:"seventy",
    80:'eighty',90:'ninety',100:'one hundred'
}

def twodigits(n):
    snum = str(n)
    l = len(snum)
    if l == 2:
        if n <20 and n>10:
            output = double[int(n)]
        elif snum[1] != '0':
            output = Zeros[int(snum[0]+'0')] + ' ' + single[int(snum[1])]
        else:
            output = Zeros[int(snum[0]+'0')]
        return output

def NUMtoWORD(n):
    snum = str(n)
    l = len(snum)
    if l == 1:
        return single[n]
    elif l == 2:
        return twodigits(n)
    elif l == 3:
        if snum[1] == '0' and snum[2] == '0':
            return single[int(snum[0])] + ' hundred'
        elif int(snum[1]+snum[2])<10 and int(snum[1]+snum[2])>0:
            return single[int(snum[0])] + ' hundred and ' + single[int(snum[1]+snum[2])]
        else:
            return single[int(snum[0])] + ' hundred and ' + twodigits(int(snum[1]+snum[2]))
    elif n == 1000:
        return triple[n]
    
            
def lenletter(n):
    word = NUMtoWORD(n)
    return len(word.replace(' ',''))

count = 0
for i in range(1,1001):
    count += lenletter(i)

print(count)



