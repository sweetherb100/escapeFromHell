'''
Given an input string, reverse the string word by word.

Example:
Given s = "the sky is blue",
return "blue is sky the".

A sequence of "non-space" characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
'''


class Solution:
    # @param A : string
    # @return string
    def reverseWords2(self, A):
        # A = "    Hello    World   Geek    "
        D = A.split()
        # D = ['Hello', 'World', 'Geek']

        E = D[::-1] #REVERSE THE STRING
        # E = ['Geek', 'World', 'Hello']

        F = ' '.join(E)
        # F = 'Geek World Hello'
        return F




solution = Solution()
# print(solution.reverseWords("the sky is blue"))
print(solution.reverseWords2("the sky is blue"))

'''
    def reverseWords(self, A):

        tempword = ""
        wordlist = []
        result = ""

        for i in range(len(A)):
            if A[i] != " ":
                tempword = tempword + A[i]
            elif A[i] == " " and tempword != "":
                wordlist.append(tempword)
                tempword = ""  # reset

        # Exception : "bb" (when there is only one word)
        if tempword != "":
            wordlist.append(tempword)

        for i in range(len(wordlist)):
            result = wordlist[i] + " " + result

        return result[0:len(result) - 1]

'''