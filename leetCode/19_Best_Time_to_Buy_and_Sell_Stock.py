'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #[7, 1, 5, 3, 6, 4]
        bestprofit = 0  # initial is 0 (no transaction is done if there is no profit)
        bestindex = len(prices)-1

        # OPTIMIZED USING 1 FOR LOOP
        # keeping bestindex (from the back) and keeping bestprofit
        for i in range(len(prices) - 1, -1, -1):  # starting from the back
            if (prices[i]-prices[i-1] > prices[bestindex]-prices[i-1]) and (prices[i]-prices[i-1] > bestprofit):
                bestindex=i
                bestprofit = prices[i]-prices[i-1]

            elif prices[bestindex]-prices[i-1] > bestprofit:
                bestprofit = prices[bestindex] - prices[i - 1]

            print("bestprofit :" + str(bestprofit))
            print("bestindex :" + str(bestindex))


        return bestprofit



solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
