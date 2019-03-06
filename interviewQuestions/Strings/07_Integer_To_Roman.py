'''
Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version
Input is guaranteed to be within the range from 1 to 3999.

Example :
Input : 5
Return : "V"

Input : 14
Return : "XIV"

Input : 1804
Return : "MDCCCIV"
'''

### CAN SAVE SOME INFORMATION IN ADVANCE IN VECTOR (2 vectors linked with index)
class Solution:
    def intToRoman(self, A):
        result = ""

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] #SHOULD BE DECREASING ORDER!!
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        for i in range(len(values)):
            result += (A // values[i]) * numerals[i] #(A // values[i]) is count of that numerals[i]
            A = A % values[i] #update A as remainder (literally remainder/the rest) #####ALWAYS DON'T FORGET!!

        return result

solution = Solution()
print(solution.intToRoman(1804))