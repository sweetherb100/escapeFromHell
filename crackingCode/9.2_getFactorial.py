'''
*Question
get Factorial

*Idea
Dynamic Programming (Recursion)
'''


def getFactorial(n):
    if n == 0 :
        return 1
    else:
        return getFactorial(n-1)*n

print(getFactorial(4))