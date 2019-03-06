'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

# Combination with dict (hashmap) and stack
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')',
                '[': ']',
                '{': '}'}

        #Exception:
        if len(s) == 0:
            return True #valid
        stack = []

        for i in range(len(s)):
            if s[i] in dict: #one of the key
                stack.append(s[i])
            elif s[i] in dict.values(): #shouldnt write else!
                if s[i] is not dict[stack.pop()]:
                    return False

        return True


solution = Solution()
print(solution.isValid("([)]"))


# Example 1:
# Input: "()"
# Output: true
# Example 2:
# Input: "()[]{}"
# Output: true
# Example 3:
# Input: "(]"
# Output: false
# Example 4:
# Input: "([)]"
# Output: false
# Example 5:
# Input: "{[]}"
# Output: true