'''
*Question :
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Testcase :
1) pwwkew -> wke (3)

'''

#strategy: 'sliding window'
# no for loop for each character but only move by the 2 indices of sliding window

class Solution:
    def lengthOfLongestSubstring(self, s):
        lidx = 0
        ridx = 0
        chset=set() #set are the characters within my sliding window
        listresult=[] #vector of string
        result=""

        while (lidx <= len(s)-1 and ridx <= len(s)-1) :
            if s[ridx] not in chset: #never visited before (wider)
                chset.add(s[ridx])
                ridx+=1

            else: # already visited (shorter)
                listresult.append(s[lidx:ridx])
                chset.remove(s[lidx]) #remove first visited character (in the next loop, the duplicate will be in the set)
                lidx += 1

        # don't forget to update the last one as well
        if ridx == len(s):
            listresult.append(s[lidx:ridx])

        # look for the maximum length among candidates
        maxlen=0
        print(listresult)
        for i in range(len(listresult)): #for loop in listresult: O(N)
            if len(listresult[i]) > maxlen:
                maxlen=len(listresult[i])
                result=listresult[i]

        return result

sl = Solution()
# print(sl.lengthOfLongestSubstring("pwwkew"))
# print(sl.lengthOfLongestSubstring("abcde"))
# print(sl.lengthOfLongestSubstring("abcabcbb"))
print(sl.lengthOfLongestSubstring("dvdf")) #3
print(sl.lengthOfLongestSubstring("abba")) #3
print(sl.lengthOfLongestSubstring("aab")) #2
print(sl.lengthOfLongestSubstring("bbbbbb")) #3