'''
*Question
get Power

*Idea
Dynamic Programming (Recursion)
'''


def getPower(n, m):
    if m == 0 :
        return 1
    else:
        return getPower(n, m-1)*n

print(getPower(2,3))


'''
Find if Given number is power of 2 or not. 
More specifically, find if given number can be expressed as 2^k where k >= 1.
return 1 if the number if a power of 2 else return 0


class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        if int(A)%2 == 1:
            return 0
        elif int(A) ==2:
            return 1
        elif int(A)==1:
            return 0
        else:
            return self.power(int(A)//2)
'''