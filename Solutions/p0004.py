"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def ifpalindrome(n):
    res = [int(i) for i in str(n)]
    rev = []
    for i in range(1,len(res)+1):
        rev.append(res[-i])
    if res == rev:
        return True
    else:
        return False 

palindrome = []
lower = 100
upper = 999   
for i in range(lower,upper+1): 
    for j in range(lower,upper+1):
        multiple = i * j
        if ifpalindrome(multiple) == True and multiple not in palindrome:
            palindrome.append(multiple)
        
print(max(palindrome))
