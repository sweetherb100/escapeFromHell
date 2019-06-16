''' 
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

        # [COMPARE] 14_longestSubstrWithoutRepeatingChars
        # step1: going through each character from the first element
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]]=i #save index of first visited
                ### should compare from the first

            else: #step2: if s[i] in dict (i.e. the character is revisited)
                print(s[dict[s[i]] : i+1]) #original appeared index ~ current index (CAREFUL! NEED TO ADD +1)
                print(s[i : dict[s[i]]-1 : -1]) #current index ~ original appeared index BACKWARD (CAREFUL! NEED TO ADD -1)
                print("**************")

                if s[dict[s[i]] : i+1] == s [i : dict[s[i]]-1 : -1]: #step3: If the substr is palindrome (should +1 and should -1)

                    # step4: update maximum length
                    if len(s[ dict[s[i]] : i+1]) > maxlength: #should +1 because should include the last index i as well
                        maxlength=len(s[ dict[s[i]] : i+1]) #update maxlength
                        result = s[ dict[s[i]] : i+1] #update result

        return result


sl=Solution()
print(sl.longestPalindrome("babababab"))

