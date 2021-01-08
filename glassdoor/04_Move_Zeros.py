'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this "in-place" without making a copy of the array.
Minimize the total number of operations.
'''

### let nums run as it is in for loop
### but keep track of number of zeros and current position to write the numbers

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur] = nums[i]
                cur += 1
            else:
                count += 1

        for i in range(count):
            nums[cur] = 0
            cur += 1

        return nums

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
