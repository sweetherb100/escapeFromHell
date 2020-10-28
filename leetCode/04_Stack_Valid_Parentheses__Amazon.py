'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        dicmap = {'(': ')',
                  '[': ']',
                  '{': '}'}


        #Exception: not enough to make paired parenthesis ("(")
        if len(s) <= 1:
            return False

        stack = []  # FILO

        for i in range(len(s)):
            if s[i] in dicmap.keys():
                stack.append(s[i])  # same as push
            if s[i] in dicmap.values():  # pop
                if len(stack) ==0: #Exception: "))"
                    return False
                if s[i] is not dicmap[stack.pop()]: #len(stack)!=0
                    return False


        if len(stack) != 0:  #Exception: "(("
            return False

        return True
solution = Solution()
print(solution.isValid("([)]"))
print(solution.isValid("))"))
print(solution.isValid("()[]{}"))

stack=[0,1,2,3] #FILO
print(stack.pop())
stack.append(4)
print(stack.pop())

dicmap = {'(': ')',
          '[': ']',
          '{': '}'}
print(dicmap.keys())
print(dicmap.values())
print(dicmap.items())