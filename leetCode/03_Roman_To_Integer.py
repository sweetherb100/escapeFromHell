# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum=0
        #apply 6 exceptions
        if "IV" in s:
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