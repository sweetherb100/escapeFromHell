'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0

        for index in range(len(nums)):
            temp=nums[index]
            for index2 in range(index+1,len(nums),1):
                temp=temp+nums[index2]
                if max < temp:
                    max=temp
        return max


solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))