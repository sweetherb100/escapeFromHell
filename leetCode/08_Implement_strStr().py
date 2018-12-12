'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack :
            return haystack.find(needle)

        return -1

solution = Solution()
print(solution.strStr("hello","llo"))


'''
        if len(haystack) ==0 : #empty string
            return 0

        if needle not in haystack:
            return -1

        # string is like a list
        if needle in haystack:
            print("Yes")
            sublen = len(needle)
            for index in range(len(haystack)):
                if haystack[index:index+sublen] == needle:
                    return sublen
'''