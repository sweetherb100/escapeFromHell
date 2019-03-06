'''
Given an array of "sorted" integers and another non negative integer k, 
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

 Example: Input : 
    A : [1 3 5] 
    k : 4
 Output : YES as 5 - 1 = 4 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.
'''

### THERE IS A REASON WHY IT IS ALREADY SORTED!!!!
### USE TWO POINTERS!!!

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def diffPossible(self,A,B):
        # [ 1, 2, 3 ], 0
        i = 0
        j = i+ 1 #j assumes to be ahead than i

        while j < len(A):  # stop when j == len(A)

            if A[j] - A[i] == B : #and i != j: BUT ISNT THIS IMPLIED??
                return 1

            elif A[j] - A[i] > B:  # no meaning to increase j
                i+=1
                j=i+1

            elif A[j] - A[i] < B:  # needed to be increased
                j += 1
        return 0


'''
### DOESNT WORK!!
if (A[i]-B) in A is true : it might be itself! (doesn't check i!=j part)
[2,3,4], 0 : False but this algorithm returns True

    def diffPossible2(self, A, B):
        if len(A) < 2:
            return 0

        for i in range(len(A) - 1, -1, -1):
            if (A[i] - B) in A:
                return 1

        return 0
'''

solution = Solution()
print(solution.diffPossible([ 1, 2, 2, 3, 4 ], 0))
print(solution.diffPossible([1,2,3], 0))
print(solution.diffPossible([2,3,4], 0))