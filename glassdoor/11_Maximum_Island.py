'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

*Data Structure : Stack (Depth First Search)
* Algorithm: RECURSION or ITERATIVE

*Algorithm
step 1) double for loop to go through each coordinate
step 2) if it is 1 and has not been visited : 
    push to the stack
step 3) pop it and check it is connected in 4 direction
step 4) whichever is connected, push to the stack
step 5) compare with the best answer so far
'''

# RECURSION
class Solution(object):
    def maxAreaOfIsland(self, grid):
        result = []
        for i in range(len(grid)): #need to traverse the whole grid
            for j in range(len(grid[0])):
                visited =set()
                val=self.maxAreaOfIsland_helper(grid, i,j, visited) #i,j : starting coordinate, visited: visited coord at that iteration
                if val != 0:
                    result.append(val)

        return max(result)

    def maxAreaOfIsland_helper(self, grid, row, col, visited):
        #base condition: when it is finished
        if row <0 or row >=len(grid) or col < 0 or col >=len(grid[0]) :#out of index ### I SHOULD WRITE grid[0]
            return 0

        if grid[row][col] == 0 : #no island
            return 0

        if (row,col) in visited:  # already visited ### SO STUPID! NOT grid[row][col] in visited!!!
            return 0

        visited.add((row,col)) ###SO STUPID! NOT vset.add(grid[row][col])

        #area : default 1 at this point because the val is 1
        area= 1+ self.maxAreaOfIsland_helper(grid, row+1, col, visited)\
              +self.maxAreaOfIsland_helper(grid, row-1, col, visited) \
              +self.maxAreaOfIsland_helper(grid, row, col+1, visited)\
              + self.maxAreaOfIsland_helper(grid, row, col-1, visited)
        return area


#### BUT THIS IS INTERMEDIATE.... HOW CAN I ADD +1?
# if grid[row][col]== 1: #island to count, count and finish
#     return 1

# need to keep track what is visited
### FOR MAXIMUM ISLAND : IT IS NOT RECOMMENDED TO USE '' AND CHANGE IT BACK
### SHOULD CHANGE IT BACK BECAUSE I NEED TO KEEP TRACK OF THE WHOLE HELPER VISITED ONE
### BETTER TO USE SET!
# temp = grid[row][col]
# grid[row][col]=''

sol=Solution()
print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                           [0,0,0,0,0,0,0,1,1,1,0,0,0],
                           [0,1,1,0,1,0,0,0,0,0,0,0,0],
                           [0,1,0,0,1,1,0,0,1,0,1,0,0],
                           [0,1,0,0,1,1,0,0,1,1,1,0,0],
                           [0,0,0,0,0,0,0,0,0,0,1,0,0],
                           [0,0,0,0,0,0,0,1,1,1,0,0,0],
                           [0,0,0,0,0,0,0,1,1,0,0,0,0]])) #6



class Solution2(object):
    #ITERATIVE
    def maxAreaOfIsland(self, grid):
        seen = set() #saved as tuple (i.e. coordinate of 2-dim)
        ans = 0

        for r0 in range(len(grid)):
            for c0 in range(len(grid[r0])): #2-dimen matrix
                if grid[r0][c0] == 1 and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)] #saved as tuple (coordinate)
                    seen.add((r0, c0)) #saved as tuple (coordinate)

                    while stack:
                        (r, c) = stack.pop() #pop as tuple
                        shape += 1
                        for (nr, nc) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)): #(nr, nc) is one of 4 tuples and only 4 search
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == 1 and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape) #update with the best area
        return ans

sol=Solution2()
print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                           [0,0,0,0,0,0,0,1,1,1,0,0,0],
                           [0,1,1,0,1,0,0,0,0,0,0,0,0],
                           [0,1,0,0,1,1,0,0,1,0,1,0,0],
                           [0,1,0,0,1,1,0,0,1,1,1,0,0],
                           [0,0,0,0,0,0,0,0,0,0,1,0,0],
                           [0,0,0,0,0,0,0,1,1,1,0,0,0],
                           [0,0,0,0,0,0,0,1,1,0,0,0,0]])) #6
