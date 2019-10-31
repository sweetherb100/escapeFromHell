'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. 
Please note that your returned answers (both index1 and index2 ) are "not zero-based". 

Put "both these numbers in order in an array" and return the array from your function 
Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. 
If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        dic = {}

        for i in range(len(A)): #index will not be duplicated because it is going through for loop
            if B - A[i] not in dic: #time to put old
                if A[i] not in dic: # old will be minimum
                    dic[A[i]] = i + 1 #not zero-based, save possible old candidate

            else: #old already exist, time to put new
                return [dic[B - A[i]], i + 1] #not zero-based

        return []


solution = Solution()
print(solution.twoSum([ 10, -3, 5, -7, -4, 5, 6, -7, 8, -5, 8, 0, 8, -5, -10, -1, 1, -6, 4, -1, -2, -2, 10, -2, -4, -7, 5, 1, 7, -10, 0, 5, 8, 6, -8, 8, -8, -8, 3, -9, -10, -5, -5, -10, 10, -4, 8, 0, -6, -2, 3, 7, -5, 5, 1, -7, 0, -5, 1, -3, 10, -4, -3, 3, 3, 5, 1, -2, -6, 3, -4, 10, -10, -3, -8, 2, -2, -3, 0, 10, -6, -8, -10, 6, 7, 0, 3, 9, -10, -7, 8, -7, -7 ],
-2))
#[3, 4]

'''
dict = {}
for i in range(len(A)):
    #if B - A[i] in A: #### THIS DOESN'T NEEDED TO BE INCLUDED FOR OPTIMIZATION PURPOSE
        if B - A[i] not in dict:  # time to put index1 (A[i] is index1)
            if A[i] not in dict:  # save the minimum index1
                dict[A[i]] = i + 1  # not zero-based
        else:  # save the minimum index2
            return [dict[B - A[i]], i + 1]
            # i+1 will be index2 (not zero-based)

return []

'''