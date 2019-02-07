'''
*Question :
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Testcase :
1) pwwkew -> wke (3) not pwke

'''

class Solution:
    # use Set to save visited char (find in vector takes more complexity)
    # use vector of vector to save substr
    def lengthOfLongestSubstring(self, s):
        hashSet=set()
        listresult=[] #vector of vector
        tempstr=""
        result=""

        for i in range(len(s)): #for loop in s: O(N)
            if s[i] not in hashSet:
                hashSet.add(s[i])
                tempstr+=s[i]
            else: #if s[i] in hashSet
                listresult.append(tempstr) #save previous one
                tempstr=s[i] #reset with new char
                hashSet.clear()
                hashSet.add(s[i]) #reset with new char

        maxlen=0
        for i in range(len(listresult)): #for loop in listresult: O(N)
            if len(listresult[i]) > maxlen:
                maxlen=len(listresult[i])
                result=listresult[i]

        print(result)

sl = Solution()
print(sl.lengthOfLongestSubstring("pwwkew"))

'''
def lengthOfLongestSubstring(self, s):
    result = 0

    OPTIMIZED 2 FOR LOOPS
    for i in range(len(s)):
        temp = []
        temp.append(s[i])
        for j in range(i + 1, len(s), 1):
            if s[j] not in temp:
                temp.append(s[j])
            else:
                if result < len(temp):
                    result = len(temp)
                    print(temp)
                    break

    print(result)
'''