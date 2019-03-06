'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Example :

Input : [1 2]
Return :  1
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        # Exception
        if len(A) == 0:
            return 0

        maxprofit = 0
        start = A[0]

        for i in range(1, len(A), 1):
            maxprofit = max(A[i] - start, maxprofit) #one transaction
            start = min(start, A[i])

        return maxprofit


solution = Solution()
print(solution.maxProfit([1,2]))