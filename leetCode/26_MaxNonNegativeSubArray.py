'''
Find out the maximum sub-array of 'non negative' numbers from an array.
The sub-array should be 'continuous'. 
That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. 
Sub-array A is greater than sub-array B if sum(A) > sum(B).

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

A : [ 0, 0, -1, 0 ]
0 0
 
NOTE1: If there is a tie, then compare with segment's length and return segment which has 'maximum length'
NOTE2: If there is still a tie, then return the segment with minimum starting index
'''

# strategy: negative number plays as partition
class Solution:
    def maxSubArray(self, arr):
        dict={} #dict key: sum, dict value: subarray
        tempsum = 0
        tempsubarray = []

        for i in range(len(arr)):
            if arr[i] >= 0:
                tempsum += arr[i]
                tempsubarray.append(arr[i])
            else: #if negative
                if tempsum not in dict: #first time of tempsum
                    dict[tempsum] = tempsubarray
                else :
                    if len(dict[tempsum]) < len(tempsubarray): #NOTE1, NOTE2:
                        dict[tempsum] = tempsubarray

                tempsum = 0 # reset
                tempsubarray = []

        ### BE CAREFUL! I should add the last tempsubarray to dict!!
        if len(tempsubarray) != 0:
            if tempsum not in dict:
                dict[tempsum] = tempsubarray
            else:
                if len(dict[tempsum]) < len(tempsubarray):  #NOTE1, NOTE2:
                    dict[tempsum] = tempsubarray


        # find maximum sum from hashmap key
        maxsum = max(dict.keys())
        return dict[maxsum]

    def maxSubArray2(self, arr):
        n=len(arr)
        # Initialize result
        res = 0

        # Traverse array
        for i in range(n):

            # Count of current
            # non-negative integers
            curr_count = 0
            while (i < n and arr[i] >= 0):
                curr_count += 1
                i += 1

            # Update result if required. (if negative)
            res = max(res, curr_count)

        return res

solution = Solution()
print(solution.maxSubArray([1, 2, 5, -7, 2, 3]))
print(solution.maxSubArray2([1, 2, 5, -7, 2, 3]))