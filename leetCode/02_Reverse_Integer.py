# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
import math

class Solution(object):
    def reverse(self, x):
        #step1: expectional cases
        if (x<-231 or x> 231-1):
            print("out of range")
            return 0

        #step2: consider the sign
        sign=1
        if(x<0):
            sign=-1
            x=-x

        digitArray= self.getDigitArray(x, [])
        lennum = len(digitArray)

        temp = 0
        # 1534 => [1, 5, 3, 4] => goal: 4351
        for i in range(lennum-1, -1, -1):
            temp+=digitArray[i]*(10**i)

        return temp*sign


    #1534 => [1, 5, 3, 4]
    def getDigitArray(self, n, list): # recursive way to get each digit in array
        if 0 <= n and n <= 9:  # if quotient is 1 digit
            list.append(n)
            return list

        else:
            self.getDigitArray(n // 10, list) #quotient, recursive
            list.append(n % 10) #remainder
            return list



solution = Solution()
print(solution.reverse(-150))
print(solution.reverse(-149))

'''
#method2: Umm... but not intuitive...
    def reverse2(self, x):

        #step1: exceptional cases
        if (x < -231 or x > (231 - 1)):
            print("out of range")
            return 0

        sign = True
        #step2: consider the negative number
        if (x < 0):
            sign = False
            x = -x  # change x as positive for now

        #step3: extract each digit (can be done with recursion)
        lennum = int(math.log10(x))+1 #get the length; not recommended because it involves conversion:len(str(x))
        digit = []
        temp = x
        for i in range(lennum - 1, -1, -1):  #if lennum=3, then i=2, 1, 0
            dig = temp // (10 ** i)  # quotient
            digit.append(dig)
            temp = temp - (dig * (10 ** i))
        #digit =[1,5,3]

        #step4: construct number by adding each digit from the back
        temp = 0
        for i in range(lennum-1, -1, -1):  #starting from the back until index 0
            temp = temp + digit[i] * (10 ** i)
        #temp=351

        if sign is False:
            temp = -temp

        return temp
'''


