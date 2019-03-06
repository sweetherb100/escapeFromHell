'''
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

https://www.youtube.com/watch?v=21OuwqIC56E
'''


class Solution:
    # @param A : string
    # @return a list of strings
    def __init__(self):
        self.result = []
        self.mapping = {"0": "0",
                        "1": "1",
                        "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz"}


    def letterCombinations(self, digits):  # digits: 23
        self.combi_helper(digits, 0, "")
        return self.result ##### DONT FORGET THIS IN THE LAST!!!


    def combi_helper(self, digits, start, combi):
        # base condition
        if start == len(digits):
            self.result.append(combi[::]) #copy by values the string
            return

        # recursive
        letters = self.mapping[digits[start]] #when start=0 (i.e. digits[start]="2")
        for i in range(len(letters)):  # abc
            self.combi_helper(digits, start+1, combi+letters[i]) #with combi="a", increase the start index


sol= Solution()
print(sol.letterCombinations("23"))