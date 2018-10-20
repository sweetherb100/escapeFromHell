'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexresult=[]

        for i in range(len(nums)):
            j=i+1
            while (j < len(nums)):
                if (nums[i]+nums[j] == target):
                    indexresult = [i, j]
                    break
            if (len(indexresult) != 0):
                break
        return indexresult

solution = Solution()
print(solution.twoSum([2,7,11,15],9))




