'''
sum("101", "10") -> "111"
#inputs :2 strings
#ouput : string

#data structure: vector
#start from the very end and go front each loop
1st : 1 + 0 =1
2nd : 0 + 1 = 1
if any of the length is left, I will add the left-over

## carry 
e.g. 111, 11
1st : 1+1 + carry(=0) = 0 (becomes carry =1)
2nd : 1+1 + carry(=1) =1 (becomes carry=1)
3th : 1 + carry(=1) = 0 (becomes carry=1)
4th: carry=1
1010
'''

class Solution:

    def sum_binary(self,str1, str2):
        max_len = max(len(str1), len(str2)) # 5(11111)
        carry=0
        result=""

        str1 = str1.zfill(max_len) # 11111
        str2 = str2.zfill(max_len) # 00011
        # zfill : add 0 to the left

        # str1[i] = str(temp % 2) => 'str' object does not support item assignment
        # python string is "immutable" (can access but cannot be changed, 변경할 수 없는)

        for i in range(max_len-1, -1, -1): #start from the back
            temp = int(str1[i]) + int(str2[i]) + carry  # 0, 1, 2, 3
            result = str(temp % 2) + result

            if temp >= 2:  # it means I have carry
                carry = 1
            else:
                carry = 0

        if carry == 1:
            result = "1" + result

        return result


    # can be optimized (have lots of duplicate lines)
    def sum_binary2(self,str1,str2):
        carry=0
        endpos1=len(str1)-1
        endpos2=len(str2)-1
        result=""

        #111 11 = 2 (0,carry=1) 3(1, carry=1)
        while endpos1 >=0 and endpos2 >=0 :
            temp= int(str1[endpos1]) + int(str2[endpos2]) + carry #0, 1, 2, 3
            result =str(temp%2) + result

            if temp >= 2: #it means I have carry
                carry=1
            else:
                carry=0

            endpos1-=1
            endpos2-=1

        #carry=1 1 = 0 (carry=1)
        #just in case, there are leftovers
        while endpos1 >=0 :
            temp= int(str1[endpos1]) + carry #0, 1, 2, 3
            result =str(temp%2) + result

            if temp >= 2: #it means I have carry
                carry=1
            else:
                carry=0

            endpos1-=1


        while endpos2 >=0 :
            temp= int(str2[endpos2]) + carry #0, 1, 2, 3
            result =str(temp%2) + result

            if temp >= 2: #it means I have carry
                carry=1
            else:
                carry=0

            endpos2-=1

        if carry==1:
            result=str(1) + result


        return result

solution = Solution()
print(solution.sum_binary('11111','1'))