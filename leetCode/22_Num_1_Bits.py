'''
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:
The 32-bit integer 11 has binary representation
00000000000000000000000000001011
so the function should return 3.
'''

class Solution:
    # @param A : integer
    # @return an integer

    # recursive
    def numSetBits(self, A):
        if A ==2 : #as bit: 10
            return 1
        elif A ==1: #as bit: 1
            return 1
        elif A==0: #as bit: 0
            return 0
        else :
            return self.numSetBits(A//2) + A%2