'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

#strategy: start from the last index
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        cur1=m-1 #last index of array1
        cur2=n-1 #last index of array2
        index=len(nums1)-1 #last index of nums1

        #while valid index (until index 0)
        while cur1 >=0 and cur2 >= 0: #stop when cur1 < 0 or cur2 < 0:
            if nums1[cur1] <= nums2[cur2]:
                nums1[index]=nums2[cur2]
                index-=1
                cur2-=1
            else:
                nums1[index] = nums1[cur1]
                index-=1
                cur1-=1

        # problem occurs when cur2 has not been reached to the front (cur2 != -1)
        # need to update the rest of nums2 to nums1

        #problem already solved when cur2 == -1 because cur1 can stay where it is

        while cur2 >= 0: #stop when cur2 == -1:
            nums1[index]=nums2[cur2]
            index-=1
            cur2-=1

        return nums1


solution = Solution()
print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(solution.merge([4,5,6,0,0,0],3,[1,2,3],3)) #when cur2 has not been reached to the front
print(solution.merge([1,2,3,0,0,0],3,[4,5,6],3))
print(solution.merge([1,3,5,0,0,0],3,[2,4,6],3))
print(solution.merge([2,4,6,0,0,0],3,[1,3,5],3))