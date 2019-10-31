'''
Given an array S of n integers, 
find three integers in S such that the sum is "closest" to a given number, target. 
Return the sum of the three integers.

Assume that there will only be one solution

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''

class Solution:
    def threeSumClosest(self, A, B):
        ## closest : approach with abs (i.e. diff)
        ## Exception : if the array is less than size 3
        ## can we have the sum same as B?;  YES SHOULD CLARIFY THIS PART

        A.sort()  # needed to be sorted!! compplexity O(n^2)

        diff = abs(A[0] + A[1] + A[2] - B)
        result = A[0] + A[1] + A[2]  # NOT AS B, IN CASE OF [ -10, -10, -10 ]

        for i in range(len(A) - 2):
            startpos = i + 1
            endpos = len(A) - 1

            while (startpos < endpos):
                if abs(A[i] + A[startpos] + A[endpos] - B) < diff:
                    diff = abs(A[i] + A[startpos] + A[endpos] - B)
                    result = A[i] + A[startpos] + A[endpos]
                elif abs(A[i] + A[startpos] + A[endpos]) == B:
                    return A[i] + A[startpos] + A[endpos] #if it is equal, literally the optimal one

                if A[i] + A[startpos] + A[endpos] < B: #needed to be increased
                    startpos += 1
                elif B < A[i] + A[startpos] + A[endpos]: #needed to be dereased
                    endpos -= 1

        return result

solution = Solution()
print(solution.threeSumClosest([ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]))
