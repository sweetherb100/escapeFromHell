'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.\

For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.

https://www.youtube.com/watch?v=LxwiwlUDOk4
https://www.youtube.com/watch?v=sz1qaKt0KGQ
'''

class Solution:
    # @param A : integer
    # @return a list of strings
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):
        self.paren_helper(n, 0, "")
        return self.result

    def paren_helper(self, open_avail, close_avail, paren):
        #base condition
        if open_avail == 0:  # I used all the available open bracket
            paren += ")" * close_avail
            self.result.append(paren[::])  # copy by value the string
            return

        # 1 recursion
        elif close_avail == 0:  # definately should start wih open bracket
            self.paren_helper(open_avail - 1, close_avail + 1, paren + "(") #used open

        # 2 recursion
        else:
            self.paren_helper(open_avail - 1, close_avail + 1, paren + "(")
            self.paren_helper(open_avail, close_avail - 1, paren + ")") #used close

sol= Solution()
print(sol.generateParenthesis(3))

