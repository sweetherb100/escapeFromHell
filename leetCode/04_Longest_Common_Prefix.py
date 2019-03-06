'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minstr = min(strs) #flight, alphabetically min
        maxstr = max(strs) #flower, alphabetically max (already sorted)
        # in between, doesn't matter because it is already sorted

        for i in range(len(minstr)):
            if minstr[i] != maxstr[i]: #I ASSUMED TO HAVE DIFFERENT WORDS BUT IT MAY BE ALL SAME
                return minstr[:i] #return string of the previous

        return minstr #Exception : ["aa","a"]

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"])) #fl
print(solution.longestCommonPrefix(["c","c"])) #c
print(solution.longestCommonPrefix(["aa","a"])) #a

# METHOD 1
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Longest Common Prefix.
# Memory Usage: 11.1 MB, less than 5.66% of Python online submissions for Longest Common Prefix.


# METHOD 2
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Longest Common Prefix.
# Memory Usage: 11 MB, less than 21.72% of Python online submissions for Longest Common Prefix.

# minstr, maxstr seems to be most clean
# def longestCommonPrefix(self, strs):
#     # Exception
#     if len(strs) == 0:
#         return ""
#
#     prefix = ""
#     # find the shortest string
#     strlen = len(strs[0])
#     for i in range(1, len(strs)):
#         if strlen > len(strs[i]):
#             strlen = len(strs[i])
#
#     contains = True
#     for i in range(strlen):
#         tempprefix = strs[0][i]
#         for j in range(1, len(strs)):
#             if tempprefix is not strs[j][i]:
#                 contains = False
#
#         # after one loop
#         if contains is True:
#             prefix = prefix + tempprefix
#
#     return prefix
