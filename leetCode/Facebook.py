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


# 1) data structure : STACK

aba

[a,b,a] 
pop: a, b, a
O(N)
STACK: O(N)

# 2) abb,a
a vs a
b vs b

a vs a => O
check isalpha
b vs b

time complexity : O(N/2) O(N)
space : O(1)
'''

#isalpha : input char, return boolean
def isPalindrome(self, str):

    ### take care of exceptional part

    startpos=0
    endpos=len(str)-1
    # a

    # abb,a
    # A,,,,,,,,b......a!!
    # a a b c d
    #for i in range(len(str)//2 + 1):
    while startpos <= endpos:
        if !self.isalpha(str[startpos]): #False
            startpos+=1 #update
            continue

        if !self.isalpha(str[endpos]): #False
            endpos-=1 #update
            continue

        # both are actually character
        if str[startpos].lower() != str[endpos].lower():
            return False

        startpos+=1
        endpos-=1


    return True
