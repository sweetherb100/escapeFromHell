'''
Given an array of integers and an integer k, 
you need to find the total number of "continuous" subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
'''


class Solution(object):
    def subarraySum(self, nums, B):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # just in case there is duplicate sum, use count as value
        dict = {}  # key: sum so far for every for loop, value: count (there can be duplicate sum)
        dict[0] = 1 #default: sum=0, its count=1
        count = 0 #total count
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum - B in dict:  # i.e. old_sum exists in dict
                count += dict[sum - B]  #### because sum - B == old_sum in dict

            # always sum should be updated in the dict
            if sum not in dict:
                dict[sum] = 1
            else:
                dict[sum] += 1

        return count


### JUST DETERMINING (NOT COUNTING)
    def subarraySum2(self, nums, B):
        ### SHOULD BE CONTINUOUS SUBARRAY
        dict = {}  # just in case there is duplicate sum, use count as value
        dict[0] = 1
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum - B in dict:  # i.e. == old_sum
                return True

                # always sum should be updated in the dict
            if sum not in dict:
                dict[sum] = 1

        return False

solution = Solution()
# print(solution.subarraySum([1,1,1],2))
# print(solution.subarraySum([1,2,3],3))
# print(solution.subarraySum([0,0,0,0,0,0,0,0,0,0],0))
print(solution.subarraySum2([1,2,3,4,5,6,7],14)) #2,3,4,5
print(solution.subarraySum2([1,2,3,4,5,6,7],20)) #2,3,4,5,6
print(solution.subarraySum2([1,2,3,4,5,6,7],8)) #False