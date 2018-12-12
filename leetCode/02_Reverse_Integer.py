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
# digits = int(math.log10(n))+1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if (x < -231 or x > (231 - 1)):
            print("out of range")
            return 0

        sign = True

        if (x < 0):
            sign = False
            x = -x  # change x as positive for now

        lennum = len(str(x))
        digit = []
        temp = x
        for i in range(lennum - 1, -1, -1):  # 2,1,0
            dig = int(temp / (10 ** i))  # quotient
            print(dig)
            digit.append(dig)
            temp = temp - (dig * (10 ** i))

        print(digit)

        temp = 0
        for i in range(lennum - 1, -1, -1):  # 2,1,0
            temp = temp + digit[i] * (10 ** i)

        if sign is False:
            temp = -temp

        print(temp)
        return temp

solution = Solution()
print(solution.reverse(-153))


'''
        if x >231-1 or x <-231 :
            return 0

        # way1 : I don't want to change into string
        if x >0:
            sign=1
            tempx=x
        else:
            sign=-1
            tempx=-x

        len=int(math.log10(tempx)) #2
        #make seperated digit array
        digits=[]
        for i in list(range(len,-1,-1)):
            digit=int(tempx/(10**i))
            digits.append(digit)
            tempx=tempx-digit*(10**i)
        # print(digits) #[1,2,3]

        # 123 -> 321
        temp = 0
        for index, digit in enumerate(digits): #(0,1),(1,2),(2,3)
            temp=temp+(10**index)*digit
        return temp*sign

        #way 2 : change into string array => reverse => attach each digits => change into int again
        # tempx=str(tempx)
        # digits=list(tempx)
        # print(tempx)
        # digitstr=''
        # for i in range(len(digits)-1,-1,-1):
        #     digitstr=digitstr+digits[i]
        # print(digitstr)
        # return int(digitstr)*sign
'''