'''
*Question :
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Testcase :
1) pwwkew -> wke (3) not pwke

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        result=0

        for i in range(len(s)):
            temp = []
            temp.append(s[i])
            for j in range(i+1,len(s),1):
                if s[j] not in temp:
                    temp.append(s[j])
                else:
                    if result < len(temp):
                        result = len(temp)
                        print(temp)
                        break

        print(result)

sl = Solution()
print(sl.lengthOfLongestSubstring("pwwkew"))



'''
start = maxLength = 0
        usedChar = {} #dictionary

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1 #reset the starting point
            else:
                maxLength = max(maxLength, (i - start) + 1)

            usedChar[s[i]] = i
            print('start ',start)
            print('maxLength ', maxLength)
            print(usedChar)
            print('*****************')

        return maxLength

'''