'''
*Question : 
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
ex) babad -> bab (aba)
babadb, babab
cbbd -> bb
'''

class Solution(object):
    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            if s[i] in s[:i] + s[i + 1:]:
                lastindex = s.rfind(s[i])
                print(lastindex)
                while (lastindex > i):  # starting from the back
                    print(s[i:lastindex + 1])
                    print(s[i:lastindex + 1][::-1])
                    if s[i:lastindex + 1] == s[i:lastindex + 1][::-1] and len(s[i:lastindex + 1]) > len(
                            result):  # including the last index as well
                        print("inside if clause")
                        result = s[i:lastindex + 1]
                        print(result)
                        break
                    else:
                        lastindex = s[i:lastindex].rfind(s[i])  # excluding the lastindex to update

        print(result)


sl=Solution()
print(sl.longestPalindrome("babab"))

'''
string = "abcde"
print(string[0:3]) #abc

res = ""
for i in range(len(s)):
    # odd case, like "aba"
    tmp = self.compare(s, i, i)
    if len(tmp) > len(res):
        res = tmp
    # even case, like "abba"
    tmp = self.compare(s, i, i + 1)
    if len(tmp) > len(res):
        res = tmp
return res


# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def compare(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]  # restore l since it has been -1. (keep r since it will return until r-1 index)

'''