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
        prefix=""
        for index in range(len(strs)-1):
            #find the shortest string
            shortestlen=len(strs[index])
            shortestindex=index
            if shortestlen > len(strs[index+1]):
                shortestindex=index+1

        contains = True
        for idx, charac in enumerate(strs[shortestindex]):
            for idx2 in range(len(strs)):
                if charac != strs[idx2][idx]:
                    contains=False
                    break
            if contains is True:
                prefix=prefix+charac
                print("prefix : " + prefix)
            else:
                break

        print(prefix)

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))