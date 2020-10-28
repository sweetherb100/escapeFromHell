'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element "always" exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        #Use hashmap to save the count of the element
        dict = {}

        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
                if dict[nums[i]] >= len(nums)//2:
                    return nums[i] #return that element

solution = Solution()
print(solution.majorityElement([1,2,2,2,2,8,11]))
