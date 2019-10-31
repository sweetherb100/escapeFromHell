'''
[EASY]
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result=[]
        visitedset=set()

        if (len(nums1) > len(nums2)):
            nums1, nums2 = nums2, nums1 #nake sure nums1 has smaller length

        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in visitedset:
                result.append(nums1[i])
                visitedset.add(nums1[i])

        return result


# Input: [1,2,2,1], [2,2]
# Output: [2]
