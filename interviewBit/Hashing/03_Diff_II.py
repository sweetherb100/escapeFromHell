'''
Given an array A of integers and another non negative integer k, 
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :
Input :
A : [1 5 3]
k : 2

Output :
1
as 3 - 1 = 2
Return 0 / 1 for this problem
'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) < 2:
            return 0

        dict={}
        for i in range(len(A)):
            if A[i] - B in dict or A[i] + B in dict: #already exist the old one
                return 1

            else : #time to save the old
                dict[A[i]]=True # keep track of visited
        return 0


solution = Solution()
print(solution.diffPossible([1,5,3],2))