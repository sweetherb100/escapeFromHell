'''
*Question
A child going up a staircase with n steps,
can hop up 1,2 or 3 steps at a time. How many ways can the child reach the top?

*Idea
Dynamic Programming (Recursion)

Time Complexity : O(3^n)
'''

def countWays(n):
    #if (n<0):
    #    return 0
    #elif n==0:
    #    return 1

    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3)

print(countWays(3))

def fibonacci(n):
    #if n < 0 :
    #    return -1

    if n==1 :
        return 0
    elif n==2 :
        return 1
    elif n>0:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))