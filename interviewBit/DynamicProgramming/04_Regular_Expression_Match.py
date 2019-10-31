'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' : Matches any single character.
'*' : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

The function prototype should be:

int isMatch(const char *s, const char *p)
Examples :

isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "*") → 1
isMatch("aa", "a*") → 1
isMatch("ab", "?*") → 1
isMatch("aab", "c*a*b") → 0
Return 1/0 for this problem.
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        curA = 0
        curB = 0
        star = -1
        match = -1

        # order might be 1) 1st and 3rd  OR 2) 2nd and 3rd
        while curA < len(A):
            if curB < len(B) and (B[curB] in (A[curA],"?")):
                curA += 1
                curB += 1

            elif curB < len(B) and B[curB] == "*":
                star = curB
                match = curA # 2 reasons needed : 1) in case they wander around the 1st clause 2) update match that might have been updated from the 3rd clause
                curB += 1 #WILL KEEP TO BACK AND FORTH WITH 2nd AND 3rd CLAUSE

            elif star != -1: #2 reasons needed : 1) in case they wandered around the 1st clause 2) updated as * in above but next one wasn't a match
                curB = star  # reset curB into star position, WILL KEEP TO BACK AND FORTH WITH 2nd AND 3rd CLAUSE
                match += 1
                curA = match  # reset curA into the match (but updated)

            else:
                return 0  # False

        ##Assuming that all A has been traversed
        while curB < len(B):
            if B[curB] != "*":
                return 0
            curB += 1

        return 1 #True when passed while clause

solution = Solution()
#True
# print(solution.isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "a**************************************************************************************"))
# print(solution.isMatch("cc", "?")) #False, go to "else"
# print(solution.isMatch("bbcbabca", "*bcba?")) #False, curB==0 (thought * covered all the strings before but there was "bcba?" left)
# print(solution.isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "*")) #True
# print(solution.isMatch("bcaabccaacc", "*c")) # True (can understand back and forth of 2nd, 3rd clause)
print(solution.isMatch("aabbaaabbbaa", "a*bbb*aa")) # True
