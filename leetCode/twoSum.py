'''
*Question : Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*Python
1) for i in nums:
i = value of nums
2) for i in range(nums):
i = index of nums
'''

class Solution(object):
    def twoSum(self, nums, target):
        result = []
        #way 1
        # for i, num in enumerate(nums):
        #     for i2, num2 in enumerate(nums):
        #         if (i != i2) and ((num + num2) == target):
        #             result.append(i)
        #             result.append(i2)
        #             return result
        # return result

        #way2
        for i,num in enumerate(nums):
            for i2 in range(i+1,len(nums)):
                if nums[i]+nums[i2] == target:
                    result.append(i)
                    result.append(i2)
                    return result
        return result

solution = Solution()
print(solution.twoSum([2,7,11,15],9))