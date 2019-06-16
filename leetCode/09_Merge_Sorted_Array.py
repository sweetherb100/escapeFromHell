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

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        ######## BE CAREFUL!!!! index should be 1 more less than the length...
        cur1=m-1
        cur2=n-1
        cur=len(nums1)-1

        #until index 0 has been taken care of1
        while cur1 >=0 and cur2 >= 0: ######### index0 included!
            if nums1[cur1] <= nums2[cur2]:
                nums1[cur]=nums2[cur2]
                cur-=1
                cur2-=1
            else:
                nums1[cur] = nums1[cur1]
                cur-=1
                cur1-=1

        print(cur1)
        print(cur2)
        # cur1 or cur2 == -1 (reached to the front)
        # problem occurs when cur2 has not been reached to the end (cur2 != -1)
        # need to update the rest of nums2 to nums1

        #problem already solved when cur2 == -1 because cur1 can stay where it is1

        while cur2 >= 0: #stop when cur2 == -1
            nums1[cur]=nums2[cur2]
            cur-=1
            cur2-=1

        return nums1




solution = Solution()
print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(solution.merge([4,5,6,0,0,0],3,[1,2,3],3))
print(solution.merge([1,2,3,0,0,0],3,[4,5,6],3))
print(solution.merge([1,3,5,0,0,0],3,[2,4,6],3))
print(solution.merge([2,4,6,0,0,0],3,[1,3,5],3))

'''
        for i in range(m, len(nums1), 1): #start from index m until end of num1
            nums1[i] = nums2[i - m]

        ### bubble sort!
        for i in range(len(nums1) - 1):
            for j in range(len(nums1) - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j] #swap

        return nums1
'''