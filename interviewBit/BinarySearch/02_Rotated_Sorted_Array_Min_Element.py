'''
Suppose a "sorted array" A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array will not contain duplicates.

Hint:"sorted array"=> try to link with Binary Search
'''


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def findMin(self, A):
        # Exception:
        if len(A) == 0:
            return -1
        elif len(A) == 1:
            return A[0]

        # Exception: if not pivoted
        if A[0] < A[-1] : #first num is smaller than the last num
            return A[0]  # already sorted but not pivoted so the smallest will be the first

        start = 0
        end = len(A) - 1

        while start <= end: #ALWAYS IN Binary Search
            mid = (start + end) // 2

            # you should feel strange to see A[start] > A[mid] even though it is "sorted"! (in fact, decreasing)
            if A[start] > A[mid]:  # min is either mid or left of mid
                if A[mid-1] > A[mid]:
                    return A[mid]
                end = mid-1 #A[mid-1] < A[mid]

            # you should feel strange to see A[mid] > A[end] even though it is "sorted"! (in fact, decreasing)
            elif A[mid] > A[end]:  # min is either mid+1 or right of mid
                if A[mid] > A[mid+1]:
                    return A[mid+1]
                start = mid+1 #A[mid] < A[mid+1]

        return -1

solution = Solution()
print(solution.findMin([4, 5, 6, 7, 0, 1, 2, 3]))

