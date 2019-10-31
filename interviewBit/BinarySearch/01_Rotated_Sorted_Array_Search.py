'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).
You are given a target value to search. If found in the array, return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

Hint:"sorted array"=> try to link with Binary Search
'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        start = 0
        end = len(A) - 1

        while start <= end:  # stop when end < start
            mid = (start + end) // 2

            if A[mid] == B:
                return mid

            # you should feel strange to see A[start] > A[mid] even though it is "sorted"!
            elif (A[start] <= B < A[mid]) or (A[start] > A[mid] and not (A[mid] < B <= A[end])): ### MAKES BIG DIFFERENCE WITH <=
                end = mid - 1

            else: # A[mid] < B <= A[end]
                start = mid + 1

        return -1

solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 4))
