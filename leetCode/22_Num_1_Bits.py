'''
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:
The 32-bit integer 11 has binary representation
00000000000000000000000000001011
so the function should return 3.
'''

#strategy: recursive
# if clause in recursive: only take care of the base expression (last part)
class Solution:
    def numSetBits(self, A):
        if A ==2 : #as bit: 10
            return 1
        elif A ==1: #as bit: 1
            return 1
        elif A==0: #as bit: 0
            return 0
        else :
            return self.numSetBits(A//2) + A%2

    def transformBits(self, A):
        if A == 2:  # as bit: 10
            return 10
        elif A == 1:  # as bit: 1
            return 1
        elif A == 0:  # as bit: 0
            return 0
        else:
            return str(self.transformBits(A//2)) + str(A % 2)

sl=Solution()
print(sl.numSetBits(11))
print(sl.transformBits(11))
print(sl.transformBits(4))
print(sl.transformBits(8))



