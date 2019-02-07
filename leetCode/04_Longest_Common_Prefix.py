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
        prefix = ""

        # find the shortest string
        strlen = len(strs[0])
        for i in range(1, len(strs)):
            if strlen > len(strs[i]):
                strlen = len(strs[i])

        contains = True
        for i in range(strlen):
            tempprefix = strs[0][i]
            for j in range(1, len(strs)):
                if tempprefix is not strs[j][i]:
                    contains = False

            # after one loop
            if contains is True:
                prefix = prefix + tempprefix

        return prefix


    #min max method
    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        print("min max method")
        print(min(strs)) #flight, alphabetically min
        print(max(strs)) #flower, alphabetically max (already sorted)

        minstr = min(strs)
        maxstr = max(strs)

        # in between, doesn't matter because it is already sorted
        for i in range(len(minstr)):
            if minstr[i] == maxstr[i]:
                continue
            else:
                return minstr[:i]



solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix2(["flower","flow","flight"]))
