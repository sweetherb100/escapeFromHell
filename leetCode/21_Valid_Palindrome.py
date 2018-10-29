'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strlist=list(s)
        print(ord("a"))
        resultlist=[]
        for i in range(len(strlist)):
            if strlist[i].isupper():
                strlist[i]=strlist[i].lower()
            if ord(strlist[i])>= 97 and ord(strlist[i])<=122:
                resultlist.append(strlist[i])

        print(resultlist)

        comparelist=resultlist
        comparelist.reverse()

        print(comparelist)
        if resultlist == comparelist:
            return True
        else:
            return False


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))