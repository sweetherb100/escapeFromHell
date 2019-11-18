'''
Given an integer array nums, find the "contiguous" subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Complexity : O(n)
'''

class Solution(object):
    def maxSubArray(self, nums):
        best = cur = nums[0]

        for i in range(1,len(nums),1):
            cur = max(cur+nums[i], nums[i]) #update cur by choosing the maximum
            best = max(best, cur) #update best by choosing the maximum

        return best



solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
