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


### Data Structure : hashmap (To make it clean as possible)
class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        dict = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}

        # problem when I is before the key V, X (e.g. IV, IX) (I = 1)
        # problem when X is before the key L, C (e.g. XL, XC) (X = 10)
        # problem when C is before the key D, M (e.g. CD, CM) (C = 100)


        ### I CAN JUST PUT VECTOR AS THE VALUES!!
        ruledict = {"I": ["V", "X"],
                    "X": ["L", "C"],
                    "C": ["D", "M"]}

        # "M D C C C I V"    1804
        sum = 0
        for i in range(len(A)-1):  # will use i+1 index. Take care the last one in the last moment
            if A[i] != "I" and A[i] != "X" and A[i] != "C": #e.g. 1, 10, 100
                sum = sum + dict[A[i]]
            else:
                if A[i + 1] not in ruledict[A[i]]:
                    sum = sum + dict[A[i]]
                else:
                    sum = sum - dict[A[i]] #then V,X (or L,C or D,M) can be just added without problem

        # Taking care of the last element (for loop was done only until len(A)-1)
        sum = sum + dict[A[len(A) - 1]]

        return sum


solution = Solution()
print(solution.romanToInt("MDCCCIV"))