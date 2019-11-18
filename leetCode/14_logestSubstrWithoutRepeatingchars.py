'''
*Question :
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Testcase :
1) pwwkew -> wke (3) not pwke

'''

class Solution:
    # 'sliding window'
    # no for loop for each character but only move by the 2 indices of sliding window
    def lengthOfLongestSubstring(self, s):
        lidx = 0
        ridx = 0
        chset=set() #set are the characters within my sliding window
        listresult=[] #vector of string
        result=""


        while (lidx < len(s) and ridx < len(s)) :
            if s[ridx] not in chset: #never visited before (wider)
                chset.add(s[ridx])
                ridx+=1

            else: # already visited (shorter)
                listresult.append(s[lidx:ridx])
                chset.remove(s[lidx])
                lidx += 1

        # don't forget to update the last one as well1
        if ridx == len(s):
            listresult.append(s[lidx:ridx])


        # update maximum length
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


# # use dict to save visited char and its index
# # use Vector of string to save substr
# def lengthOfLongestSubstring(self, s):
#     dict = {}
#     listresult = []  # vector of string
#     tempstr = ""
#     result = ""
#
#     # step1: going through each character from the first element
#     for i in range(len(s)):  # for loop in s: O(N)
#         if s[i] not in dict:
#             dict[s[i]] = i  # save its first visited index
#             tempstr += s[i]
#
#         else:  # step2: if s[i] in dict
#             listresult.append(tempstr)  # step2-1: save previous one
#             print(tempstr)
#             tempstr = s[dict[s[i]] + 1: i + 1]  # step2-2: reset with new char
#             dict[s[i]] = i
#
#     ### BE CAREFUL! I should add the last tempstr to hashset!!
#     if len(tempstr) != 0:
#         listresult.append(tempstr)
#
#     # step3: update maximum length
#     maxlen = 0
#     print(listresult)
#     for i in range(len(listresult)):  # for loop in listresult: O(N)
#         if len(listresult[i]) > maxlen:
#             maxlen = len(listresult[i])
#             result = listresult[i]
#
#     return result