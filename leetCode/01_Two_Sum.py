'''
*Question : Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# OPTIMIZED WITH ONE FOR LOOP
class Solution(object):
    def twoSum(self, nums, target):
        result=[]

        # Complexity: O(N^2)
        for i in range(len(nums)): # for loop in nums: O(N)
            if target-nums[i] in nums: #find in vector: O(N)
                result=[i, nums.index(target-nums[i])] #find in vector: O(N)
                return result

        return [] #doesn't exist


#method2: Use hashMap to reduce the complexity of finding the value
#Question guarantees that there will be only unique element
    def twoSum2(self, nums, target):
        result=[]
        dict={}

        # Complexity: O(N)
        for i in range(len(nums)):
            dict[nums[i]]=i #key: element, value: index

        for i in range(len(nums)): #for loop in vector: O(N)
            if target-nums[i] in dict: #find in hashMap: O(1)
                result=[i, dict[target-nums[i]]] #access in hashMap: O(1)
                return result

        return []  # doesn't exist


solution = Solution()
print(solution.twoSum([2,7,11,15],9))
print(solution.twoSum2([2,7,11,15],9))
