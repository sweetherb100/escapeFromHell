'''
*Question : 
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
ex) babad -> bab (aba)
babaab, babab
cbbd -> bb
baabdd -> baab
babababab

'''

class Solution(object):
    #use dict to save the first visited index
    def longestPalindrome(self, s):

        dict={}
        maxlength=0
        result=""

        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]]=i #save index of first visited
                ### should compare from the first

            else: #is s[i] in dict
                print(s[dict[s[i]]: i + 1])
                print(s[i: dict[s[i]] -1 : -1])
                print("**************")
                if s[ dict[s[i]] : i+1 ] == s [ i : dict[s[i]]-1 : -1]: #should +1 and should -1; if it is paalindrome

                    if len(s[ dict[s[i]] : i+1]) > maxlength: #should +1 because should include the last index i as well
                        maxlength=len(s[ dict[s[i]] : i+1]) #update maxlength
                        result = s[ dict[s[i]] : i+1] #update result

        return result


sl=Solution()
print(sl.longestPalindrome("babababab"))



'''
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
                        lastindex = s[i:lastindex].rfind(s[i])  # excluding the last index to update

        print(result)
'''
