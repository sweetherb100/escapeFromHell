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
    # use Set to save visited char (find in vector takes more complexity)
    # use vector of string to save substr
    def lengthOfLongestSubstring(self, s):
        hashSet=set()
        listresult=[] #vector of string
        tempstr=""
        result=""

        # step1: going through each character from the first element
        for i in range(len(s)): #for loop in s: O(N)
            if s[i] not in hashSet:
                hashSet.add(s[i])
                tempstr+=s[i]

            else: # step2: if s[i] in hashSet
                listresult.append(tempstr) #step2-1: save previous one
                tempstr=s[i] #step2-2: reset with new char
                hashSet.clear()
                hashSet.add(s[i]) #reset with new char

        ### BE CAREFUL! I should add the last tempstr to hashset!!
        if len(tempstr) != 0:
            listresult.append(tempstr)

        # step3: update maximum length
        maxlen=0
        for i in range(len(listresult)): #for loop in listresult: O(N)
            if len(listresult[i]) > maxlen:
                maxlen=len(listresult[i])
                result=listresult[i]

        return result

sl = Solution()
# print(sl.lengthOfLongestSubstring("pwwkew"))
print(sl.lengthOfLongestSubstring("abcde"))
