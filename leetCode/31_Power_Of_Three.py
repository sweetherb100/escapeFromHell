'''
Given an integer, write a function to determine if it is a power of three.
(Coded in the recursive way)
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 3:
            return True
        elif n== 2:
            return False
        elif n == 1:
            return False
        else:
            return self.isPowerOfThree(n//3)

sl=Solution()
print(sl.isPowerOfThree(27))