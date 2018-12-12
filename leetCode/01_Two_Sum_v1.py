'''
*Question : Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                if nums[i]+nums[j] == target :
                    result=[i,j]
                    return result

        print("does not exist")



solution = Solution()
print(solution.twoSum([2,7,11,15],9))

'''
        result = []

        for i,num in enumerate(nums):
            for i2 in range(i+1,len(nums)):
                if nums[i]+nums[i2] == target:
                    result.append(i)
                    result.append(i2)
                    return result
        return result
'''