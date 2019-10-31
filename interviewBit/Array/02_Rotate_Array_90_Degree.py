'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note that if you end up using an additional array, you will only receive partial score.

Example:
If the array is

[
    [1, 2],
    [3, 4]
]

Then the rotated array becomes:
[
    [3, 1],
    [4, 2]
]
'''


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        N = len(A)

        # step1 : transpose the matrix
        for i in range(len(A)):
            for j in range(i+1, len(A)): #don't need to swap between i,i and just need to swap upper matrix
                A[i][j], A[j][i] = A[j][i], A[i][j]


        # step2: swap the columns
        for j in range(len(A) // 2): #swap only half column
            for i in range(len(A)): #swap each row of that column
                A[i][j], A[i][(N-1)-j] = A[i][(N-1)-j], A[i][j]

        return A

solution = Solution()
print(solution.rotate([
                    [1,  2,  3,  4],
                    [5,  6,  7,  8],
                    [9,  10, 11, 12],
                    [13, 14, 15, 16]]))

