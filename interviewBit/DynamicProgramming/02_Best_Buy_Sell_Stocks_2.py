'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example :

Input : [1 2 3]
Return : 2
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        # Exception
        if len(A) == 0:
            return 0

        bestprofit = 0
        start = A[0]

        for i in range(1, len(A), 1):
            if start > A[i]: #minimize the start (if starting point is larger, then update the starting point)
                start = A[i]
            else:  # start < A[i]
                bestprofit += (A[i] - start) #multiple transaction every time start < A[i]
                start = A[i] #updating starting point after finishing transaction

        return bestprofit

solution = Solution()
print(solution.maxProfit([1,2,3]))