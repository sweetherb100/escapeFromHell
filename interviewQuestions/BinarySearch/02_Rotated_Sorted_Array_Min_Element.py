'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array will not contain duplicates.
]'''


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
        if A[0] < A[-1] :
            return A[0]  # already sorted but not pivoted so the smallest will be the first

        start = 0
        end = len(A) - 1

        while start <= end: #ALWAYS IN BS
            mid = (start + end) // 2

            if A[start] > A[mid]:  # min on the left
                if A[mid - 1] > A[mid]:
                    return A[mid]
                end = mid - 1

            elif A[mid] > A[end]:  # min on the right
                if A[mid] > A[mid + 1]:
                    return A[mid + 1]
                start = mid + 1

        return -1

solution = Solution()
print(solution.findMin([4, 5, 6, 7, 0, 1, 2, 3]))

