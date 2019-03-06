'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

### RECURSION
### EXTRA CONDITION TO BE CONSIDERED : NEED TO KEEP TRACK OF VISITED
# FROM the board, RECURSIVE "ABCCED" -> A FOUND + "BCCED"
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i,j):
                    return True
        return False

    def exist_helper(self, board, word, row, col):
        #base condition: when it is reached the end (True)
        if len(word) == 0:
            return True

        #base condition : outside of board or not matched (False)
        if row <0 or row >=len(board) or col <0 or col >=len(board[0]) or board[row][col] != word[0]:
            return False

        # if reached at this point: board[row][col] == word[0] and it should be checked to say it is visited
        temp = board[row][col]
        board[row][col]=''

        # send word one character forward (keep slicing the word)
        # or can be used so that if 2 of them is False and 2 is True, still it is True
        result = self.exist_helper(board, word[1:], row+1, col) or\
                 self.exist_helper(board, word[1:], row - 1, col) or\
                 self.exist_helper(board, word[1:], row, col + 1) or\
                 self.exist_helper(board, word[1:], row, col - 1)

        board[row][col]=temp #return it back regardless of the result
        return result #result is boolean (True/False) connected by or


sol=Solution()
# print(sol.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "SEE"))

# print(sol.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "ABCB"))

print(sol.exist(
    [["A","B","C","E"],
     ["S","F","E","S"],
     ["A","D","E","E"]], "ABCESEEEFS"))


'''
### SIMILAR TO THE MAX ISLAND?! BUT SO MUCH EXCEPTION TO TAKE CARE IN ITERATIVE WAY.. WHAT A MESS!!!!
        # DATA STRUCTURE : STACK
        stack = []
        ### DO I NEED TO TRACK WHAT IS VISITED?
        curstack = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # finally found the first letter so lets trick it down
                    print("*********")
                    print((i,j))
                    visited = []  # reset
                    curstack.append(0)
                    stack.append((i, j))  # save it as tuple (2-dim)
                    visited.append((i, j))
                    #### SAME LETER CELL MAY NOT BE USED MORE THAN ONCE!!   MAYBE I SHOULD MAKE EXTRA MEMORY

                while stack:
                    print(stack)
                    print(curstack)
                    print(visited)
                    (ai, aj) = stack.pop()
                    wordcur=curstack.pop()
                    for (ni, nj) in ((ai - 1, aj), (ai + 1, aj), (ai, aj - 1), (ai, aj + 1)): #only 4 search
                        if wordcur == len(word)-1:
                            return True

                        if 0<=ni < len(board) and 0<=nj < len(board[0]) and (ni, nj) not in visited and board[ni][nj] == word[wordcur+1]:
                            ### should take care of index out of range
                            ###ALSO SHOULD PUT 0<= or else it can become - and look for the index from the back
                            print((ni,nj))
                            print(wordcur+1)
                            # wordcur += 1 ## SHOULD NOT UPDATE WORDCUR
                            curstack.append(wordcur+1) ## SHOULD ALSO MAKE STACK FOR WORDCUR TO KEEP TRACK OF IT AS WELL
                            stack.append((ni, nj))  # save it as tuple (2-dim)
                            visited.append((ni, nj))

                        else : #need to research
                            if len(visited) != 0:
                                visited.pop()
                            # break NEVER! I NEED TO RUN ALL 4 SEARCH TO TRACK IT BACK!!
                    # if wordcur == len(word):
                    #     return True

        return False  # didnt found after full loop

'''
