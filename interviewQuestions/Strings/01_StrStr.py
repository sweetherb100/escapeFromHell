'''
Another question which belongs to the category of questions which are intentionally stated vaguely. 
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ). 
Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases. 

'''
### ASK WHICH IS SUBSTRING/STRING
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B): #I chose A as substring, B as string
        ### DB, helloDB

        ## Exception
        if len(A) == 0 or len(B) == 0:
            return -1
        if len(A) > len(B): # substring cannot be longer than the string
            return -1

        sublen = len(A)
        for i in range(len(B)):
            if A[0] == B[i] and sublen + i <= len(B): ## SHOULD BE <=, NOT <
                if B[i:i + sublen:1] == A:
                    return i #return that index

        return -1
        # Can be out of index


solution = Solution()
print(solution.strStr("DB","helloDB"))
