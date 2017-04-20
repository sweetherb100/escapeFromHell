'''
Question :
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Testcase :
1) pwwkew -> wke (3) not pwke

Outline :
1) Unique Question : use list("XXX"), hash, ord("XX") (char->ASCII code) 
2) list("XXX") : String to list of chars
3) Don't need to change string into char list for for loop.
for char in str: still works!
4) hash=[False]*256 : initialize and set the size at the same time

My way : find number of unique chars in String
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hash = [False] * 256 #initialize and set the size at the same time
        # chars = list(s)
        result = []

        for char in s:
            if hash[ord(char)] is False:
                hash[ord(char)] = True
                result.append(char)

        print(len(result))


sl = Solution()
sl.lengthOfLongestSubstring("abcabcbb")
