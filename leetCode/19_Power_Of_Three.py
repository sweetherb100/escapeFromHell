'''
Given an integer, write a function to determine if it is a power of three.
'''

# if clause: only take care of the base expression (last part)

class Solution(object):
    def isPowerOfThree(self, n):
        if n == 3:
            return True
        elif n== 2:
            return False
        elif n == 1:
            return False
        else:
            return self.isPowerOfThree(n//3) #quotient

sl=Solution()
print(sl.isPowerOfThree(27))