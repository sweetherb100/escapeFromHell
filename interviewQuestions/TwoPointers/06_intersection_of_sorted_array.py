'''
Find the intersection of two "sorted" arrays.
i.e. 
Given 2 "sorted" arrays, find all the elements which occur in both the arrays.

Example :
Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]
Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]
Output : [3 5]
'''

### SIMILAR TO THE INTERVIEW QUESTIONS I DID BEFORE!!

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):

        ### THERE IS REASON WHY IT IS SORTED

        # A : [1 2 3 3 4 5 6]
        # B : [3 3 5]
        # Output : [3 3 5]

        apos = 0
        bpos = 0
        result = []

        while apos < len(A) and bpos < len(B):  # SHOULD BE AND!!
            if A[apos] == B[bpos]:
                result.append(A[apos])
                apos += 1
                bpos += 1

            elif A[apos] < B[bpos]:  # A should be increased (to be same as B)
                apos += 1

            elif B[bpos] < A[apos]: # B should be increased (to be same as A)
                bpos += 1

        return result

solution = Solution()
print(solution.intersect([1,2,3,3,4,5,6], [3,5]))


