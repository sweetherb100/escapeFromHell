'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero (i.e. will make the front disappear??) or more of the preceding element. (of the same one??)

The matching should cover the entire input string (not partial).

The function prototype should be:

int isMatch(const char *s, const char *p)
Some examples:

isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "a*") → 1
isMatch("aa", ".*") → 1
isMatch("ab", ".*") → 1
isMatch("aab", "c*a*b") → 1
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

### recursion and also memorization
class Solution(object):
    def __init__(self):
        self.memo = {} #hashmap is used to use (i,j) as key and True/False as value

    def isMatch(self, text, pattern):
        return self.isMatch_helper(text, pattern, 0, 0)

    def isMatch_helper(self, text, pattern, i, j):
        if (i, j) not in self.memo:
            if j == len(pattern):
                ans = (i == len(text))

            ### * only takes care of the pattern (doesnt effect the text)
            elif i < len(text) and pattern[j] in (text[i], '.'):
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = self.isMatch_helper(text, pattern, i, j + 2) or self.isMatch_helper(text, pattern, i + 1, j)
                    #check i is not part of regrex or assume i is part of regrex so check i+1 is also part of regrex
                else:
                    ans = self.isMatch_helper(text, pattern, i + 1, j + 1)

            else:
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = self.isMatch_helper(i, j + 2, text, pattern)
                    #check i is not part of regrex (cannot be part of regrex)
                else:
                    ans = False

            self.memo[(i, j)] = ans #update in the dict

        return self.memo[i, j]


solution = Solution()
print(solution.isMatch("ac", "ab*c"))
# A : "ac"
# B : "ab*c"
