'''
[Method1] data structure : STACK
but ABCBA in stack and pop each character out and compare from the front
Time Complexity: O(N)
Space Complexity: O(N)
=> BUT MAY NOT BE ALL CHARACTERS

# [Method2] Compare between the front and the end and skip as non-alphabet comes in
ABB
A vs B => not same, False
ABBA
A vs A
B vs B => after all the comparison, it is still valid, True

Time complexity : O(N/2) (=O(N))
Space complexity : O(1) (just need to save the index)
'''

class Solution():
    def isalpha(self,charac):
        if 97 <= ord(charac.lower()) and ord(charac.lower()) <= 122:
            return True
        return False

    def isPalindrome(self, str):
        startpos=0
        endpos=len(str)-1

        #for i in range(len(str)//2 + 1): NOT RECOMMENDED BECAUSE YOU DONT KNOW HOW MANY NON-ALPHA WILL BE
        while startpos <= endpos:
            if self.isalpha(str[startpos]) is False:   #!self.isalpha(str[startpos]) gives me an error (negation in Python is 'not')
                startpos+=1 #update
                continue

            if self.isalpha(str[endpos]) is False :
                endpos-=1 #update
                continue

            # both are actually character
            if str[startpos].lower() != str[endpos].lower():
                return False

            #update
            startpos+=1
            endpos-=1

        return True

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal, Panama!")) #True
print(solution.isPalindrome("a")) #True
print(solution.isPalindrome("abb,a")) #True
print(solution.isPalindrome("A,,,,,,,,b......a!!")) #True
print(solution.isPalindrome("a a b c d")) #False
