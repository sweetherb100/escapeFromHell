'''
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. 
That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. 
Sub-array A is greater than sub-array B if sum(A) > sum(B).

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

A : [ 0, 0, -1, 0 ]
0 0
 
NOTE1: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE2: If there is still a tie, then return the segment with minimum starting index
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers

    def maxSubArray(self, arr):
        ### negative num plays as partition
        dict={}
        tempsum = 0
        tempsubarray = []

        # [COMPARE] 14_logestSubstrWithoutRepeatingchars, 15_longestPalindromicSubstr

        # going through the element in the array
        for i in range(len(arr)):
            if arr[i] >= 0:
                tempsum += arr[i]
                tempsubarray.append(arr[i])
            else: #if negative

                ############### THIS IS THE KEY POINT (HOW TO TAKE CARE OF TIE)
                if tempsum not in dict: #first time of tempsum
                    dict[tempsum] = tempsubarray
                else :
                    if len(dict[tempsum]) < len(tempsubarray): #NOTE1: in case of tie, return segment which has maximum length
                        dict[tempsum] = tempsubarray #replace only when tempsubarray is longer (if not, keep the one with minimum starting index)

                tempsum = 0 # reset
                tempsubarray = []

        ### BE CAREFUL! I should add the last tempsubarray to subarrayvector!!
        if len(tempsubarray) != 0:
            if tempsum not in dict:
                dict[tempsum] = tempsubarray
            else:
                if len(dict[tempsum]) < len(tempsubarray):  #NOTE1: in case of tie, return segment which has maximum length
                    dict[tempsum] = tempsubarray  # replace only when tempsubarray is longer (if not, keep the one with minimum starting index)


        # find maximum sum from hashmap key
        maxsum = max(dict.keys())
        return dict[maxsum]

    
solution = Solution()
print(solution.maxSubArray([1, 2, 5, -7, 2, 3]))
