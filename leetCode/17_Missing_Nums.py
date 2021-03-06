'''
Given an array containing n "distinct" numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''
class Solution(object):
    def missingNumber(self, nums):

        # constant extra space
        n = len(nums)
        totalsum = n * (n + 1) / 2
        #Complexity: O(N), need to go through whole nums to get the sum of its array
        numssum=sum(nums)

        return totalsum - numssum

solution = Solution()
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))