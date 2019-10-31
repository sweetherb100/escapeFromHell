'''
Find the longest increasing subsequence of a given sequence / array.
In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order, 
and in which the subsequence is as long as possible. 
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.

Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output : 6

The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        # Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        # Output : 6

        result = []
        for i in range(len(A)):
            pos = self.BinarySearch(result, A[i])  # look for insertion index in the result
            if pos == len(result):
                result.append(A[i])
            else:  # replace
                result[pos] = A[i]

        return len(result)

    # result list should be sorted already
    def BinarySearch(self, ls, val):
        if len(ls) == 0:
            return 0

        start = 0
        end = len(ls)-1

        while start <= end:  # binary search (STOP WHEN end < start)
            mid = (start + end) // 2

            if ls[mid] < val:  # on the right
                start = mid + 1

            elif ls[mid] > val:  # on the left
                end = mid - 1

            else:  # if it is the same
                return mid

        return start # start after it become end < start


sol =Solution()
print(sol.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])) #6
# print(sol.lis([84, 80, 27]))

print(sol.BinarySearch([0,2,6,14], 1))


