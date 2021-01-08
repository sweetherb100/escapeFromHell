'''
Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example :
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        # recursive : cur_path = (left + left_path) or (down + down_path)
        return self.uniquePath_helper(A, 0, 0)  # orig, starting coordinate

        ### COUNT IS NOT NEEDED BECAUSE in the helper, returns +
        ### NEED TO PUT RETURN YOU STUPID!!

    def uniquePath_helper(self, A, row, col):
        # base condition
        if row == len(A)-1 and col == len(A[0])-1:
            return 1  # can add one unique Path

        if row >= len(A) or col>= len(A[0]) : #dont need to proceed # IT IS "OR" NOT "AND"
            # I don't need to consider row < 0 because I will only move to the left or to down (cannot be negative index)
            return 0

        if A[row][col] == 1: #dont need to proceed
            return 0

        # recursion
        # SYNTAX : need to put self.
        return self.uniquePath_helper(A, row+1, col) + self.uniquePath_helper(A, row, col+1)

sol=Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],
                                    [0,1,0],
                                    [0,0,0]]))


##### THIS IS NOT BASE CONDITION BUT JUST INTERMEDIATE CONDTION I SHOULDNT NEED TO WRITE
        ##### I DONT NEED TO PUT i+1 put just focus on the cucrent index because the recursion will take care
        # if i < len(A) and j < len(A[0]) and A[i][j] != 1:  # can go to the left without obstacle
        #     return 1
        #
        # elif i < len(A) and j < len(A[0]) and A[i][j] != 1:  # can go to the left without obstacle
        #     return 1
