'''
"A man, a plan, a canal, Panama!" -> true
"aba" -> true
"Aba" -> true
"A,,,,,,,,b......a!!" -> true

isalpha(char) -> bool
isalpha('A') -> true
isalpha(' ') -> false

#input : string
#retrun : boolean
#exception: upper case/lower case, character 
#ASCII code lower case : 97 <= <=122
#A -> lower case 


# method 1) data structure : STACK
=> BUT MAY NOT BE ALL CHARACTERS
[a,b,a] 
pop: a, b, a
O(N)
STACK: O(N)

# method 2) abb,a
a vs a
b vs b
(comma should be skipped)

time complexity : O(N/2) O(N)
space : O(1)
'''

#isalpha : input char, return boolean
class Solution():
    def isalpha(self,charac):
        if 97 <= ord(charac.lower()) and ord(charac.lower()) <= 122:
            return True
        return False

    def isPalindrome(self, str):
        ### take care of exceptional part
        startpos=0
        endpos=len(str)-1
        # TEST CASE:
        # a
        # abb,a
        # A,,,,,,,,b......a!!
        # a a b c d

        #for i in range(len(str)//2 + 1):

        while startpos <= endpos:
            if self.isalpha(str[startpos]) is False: #False  ###!self.isalpha(str[startpos]) gives me an error
                startpos+=1 #update
                continue

            if self.isalpha(str[endpos]) is False : #False
                endpos-=1 #update
                continue

            # both are actually character
            if str[startpos].lower() != str[endpos].lower():
                return False

            startpos+=1
            endpos-=1

        return True

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal, Panama!")) #True
print(solution.isPalindrome("a")) #True
print(solution.isPalindrome("abb,a")) #True
print(solution.isPalindrome("A,,,,,,,,b......a!!")) #True
print(solution.isPalindrome("a a b c d")) #False


