'''
Given an array with n objects colored red, white or blue, 
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: Using library sort function is not allowed.

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
'''


# SO SIMPLE AND EASY!!!!
### I CAN MAKE B with only 3 elements because the questions guarantees that there will be only 3 colors
class Solution:
    # @param A : list of integers
    # @return A after the sort

    def sortColors(self, A):
        B = [0, 0, 0] #initialize (3 colors)
        for i in A:
            B[i] += 1

        return [0]*B[0] + [1]*B[1] + [2]*B[2] #B[0], B[1], B[2] is the count of the color

solution = Solution()
print(solution.sortColors([0, 1, 2, 0, 1, 2]))
# [0, 0, 1, 1, 2, 2]


'''
##extra data structure :hashmap
        dict = {}  ### STUPID!! initialize!!

        for i in range(len(A)):
            if A[i] not in dict:
                dict[A[i]] = 1 #######SHOULD START FROM 1
            else:
                dict[A[i]] += 1

        # output order also should be 0, 1, 2
        # may not have one of the three!! (exception!!)
        cur = 0
        
        if 0 in dict:
            A[cur: cur + dict[0]: 1] = [0] * dict[0]
            cur = cur + dict[0]

        if 1 in dict:
            A[cur: cur + dict[1]: 1] = [1] * dict[1]
            cur = cur + dict[1]

        if 2 in dict:
            A[cur: cur + dict[2]: 1] = [2] * dict[2]

        return A
'''