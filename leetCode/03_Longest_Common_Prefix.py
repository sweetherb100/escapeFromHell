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
        minstr = min(strs) #'flight', alphabetically min
        maxstr = max(strs) #'flower', alphabetically max (already sorted)
        # in between, doesn't matter because it is already sorted

        for i in range(len(minstr)):
            if minstr[i] != maxstr[i]: #If element of index i is not the same,
                return minstr[:i] #then return string of before index i (index i not included)

        return minstr #Exception: ["aa","a"]

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"])) #fl
print(solution.longestCommonPrefix(["c","c"])) #c
print(solution.longestCommonPrefix(["aa","a"])) #a
