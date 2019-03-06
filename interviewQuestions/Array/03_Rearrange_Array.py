'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
Example:

Input : [1, 0]
Return : [0, 1]
'''

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A) #O(1) extra space
        for i in range(n): #first for loop
            # print(A)
            # print(A[A[i]])
            # print((A[A[i]]%n))
            A[i] = A[i] + (A[A[i]]%n)*n

        # print(A)
        for i in range(n): #second for loop
            A[i] = A[i]//n

        return A

solution = Solution()
print(solution.arrange([1,2,3,0,5,4]))
