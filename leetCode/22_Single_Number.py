'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1
Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

class Solution(object):

    # Use hashmap to check whether it has been visited
    def singleNumber(self, nums):
        dict={}

        for i in range(len(nums)): #for loop in nums: O(N)
            if nums[i] not in dict: #find in hashmap: O(1)
                dict[nums[i]] = False
            else:
                dict[nums[i]] = True

        for key, value in dict.items(): #for loop in dict.items(): O(N)
            if value is False:
                return key

    def singleNumber2(self, nums):
        # applying the formula: every element appears twice except for one
        return (2 * sum(set(nums)) - sum(nums))



solution = Solution()
print(solution.singleNumber([2,2,1]))
print(solution.singleNumber([2,2,3,5,3,5,1]))
print(solution.singleNumber2([2,2,3,5,3,5,1]))
