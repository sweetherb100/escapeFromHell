'''
*Question
get Digit Sum
*Idea
Dynamic Programming (Recursion)
'''


def getDigitSum(n):
    if 0 <= n and n <= 9 :#if 1 digit
        return n #return itself
    else:
        return n%10 + getDigitSum(n//10)

print(getDigitSum(12321))
#print(11//10)
#print(11/10)

def getDigitArray(n, list):
    if 0 <= n and n <= 9 :#if 1 digit
        list.append(n)
        return list
    else:
        getDigitArray(n//10, list)
        list.append(n % 10)
        return list

print(getDigitArray(12345,[]))
