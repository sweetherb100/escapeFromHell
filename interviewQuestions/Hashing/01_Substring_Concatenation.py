'''
You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
'''
### HINT 1): L has all the same length
### HINT 2) : applears only once

## EXECPTION TEST CASE
# A : "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# B : [ "aaa", "aaa", "aaa", "aaa", "aaa" ]


### BE CAREFUL!
#1) words in B can be SAME! (so using hashmap is not a good idea)

#2)  I SHOULDN'T JUMP i+wordlen because
        # CASE : A : "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        # B : [ "aaa", "aaa", "aaa", "aaa", "aaa" ]


from collections import Counter
class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if len(B) == 0:
            return []

        wordlen = len(B[0])
        subslen = len(B)
        result = []
        counter = Counter(B)  # returns value and its count

        for i in range(len(A)):
            if A[i:i + wordlen] in B:  #### BE CAREFUL!! i+wordlen
                stringlist=[]
                for index in range(i, i+wordlen*subslen, wordlen): #shouldnt look until len(A) but only length wordlen*sublen (i.e. substring concatenation)
                    stringlist.append(A[index:index+wordlen])
                #stringlist = [A[index:index + wordlen] for index in range(i, i + wordlen * subslen, wordlen)]

                if counter == Counter(stringlist):
                    result.append(i)

        return result

solution = Solution()
print(solution.findSubstring("barfoothefoobarmanbarfoobarfoofoobar", ["foo","bar"])) #[0, 9, 18, 21, 24, 30]
# print(solution.findSubstring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", [ "aaa", "aaa", "aaa", "aaa", "aaa" ]))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]