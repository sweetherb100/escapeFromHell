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
    #Kadane's algorithm can solve it in O(n) time and O(1) space
    def maxSubArray2(self, nums):
        best = cur = nums[0]

        for i in range(1,len(nums),1):
            cur = max(cur + nums[i], nums[i]) #update cur
            best = max(best, cur) #update best
        return best



solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

'''
def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max = 0

    for index in range(len(nums)):
        temp = nums[index]
        for index2 in range(index + 1, len(nums), 1):
            temp = temp + nums[index2]
            if max < temp:
                max = temp
    return max
'''