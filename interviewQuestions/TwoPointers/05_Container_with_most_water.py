'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained 
( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).
'''

class Solution():
    def maxArea(self, A):
        best = 0
        area = 0
        i=0 #starting from the left
        j=len(A)-1 #starting from the right

        while (i < j) : #STOP when i == j
            area = min(A[i], A[j])* (j-i)
            best=max(area, best)

            if A[i] < A[j]: #A[i] smaller so move A[i] and hope to find taller one
                i+=1
            else :
                j-=1

        return best

solution = Solution()
print(solution.maxArea([1, 5, 4, 3]))

'''
### Complexity : O(N^2)
    def maxArea(self, A):
        best = 0

        for i in range(len(A) - 1):
            if A[i] != 0:
                for j in range(i + 1, len(A), 1):
                    if A[j] != 0:
                        if min(A[i], A[j]) * (j - i) > best:
                            best = min(A[i], A[j]) * (j - i)

        return best

'''