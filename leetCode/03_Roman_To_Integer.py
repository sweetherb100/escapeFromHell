'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum=0
        #apply 6 exceptions
        if "IV" in s: #find substring in string
            sum=sum+4
            start=s.find("IV")
            s = s[0:start] + s[start + 2:len(s)]
            print(s)
        if "IX" in s:
            sum = sum + 9
            start = s.find("IX")
            s = s[0:start] + s[start + 2:len(s)]
            print(s)
        if "XL" in s:
            sum = sum + 40
            start = s.find("XL")
            s = s[0:start] + s[start + 2:len(s)]
            print(s)
        if "XC" in s:
            sum = sum + 90
            start = s.find("XC")
            s = s[0:start] + s[start + 2:len(s)]
            print(s)
        if "CD" in s:
            sum = sum + 400
            start = s.find("CD")
            s = s[0:start] + s[start + 2:len(s)]
            print(s)
        if "CM" in s:
            sum = sum + 900
            start = s.find("CM")
            s = s[0:start] + s[start + 2:len(s)]
            print(s)

        print(sum)

        for i in range(len(s)):
            if "I" in s[i]:
                sum=sum+1
            if "V" in s[i]:
                sum = sum + 5
            if "X" in s[i]:
                sum = sum + 10
            if "L" in s[i]:
                sum = sum + 50
            if "C" in s[i]:
                sum = sum + 100
            if "D" in s[i]:
                sum = sum + 500
            if "M" in s[i]:
                sum = sum + 1000
        print(sum)
        return sum



solution = Solution()
print(solution.romanToInt("MCMXCIV"))