'''
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
Example:

if n = 2,
the sequence is 11.
'''

### RECURSION
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        #base condition
        if A <= 1:
            return '1' #return string

        # recursion
        it = iter(self.countAndSay(A - 1)) #### should be "it"
        res = [] #reset for every recursion

        cur = next(it) ###next(it) comes out as val (not like pointer type) and cur is now the first element
        cnt = 1

        for x in it: #starting from the second element
            if x != cur:
                # flush
                res.extend([cnt, cur])
                cur = x #update cur with new different iter
                cnt = 1 #reset
            else: # x==cur
                cnt += 1

        # Flush last one (### DON'T FORGET TO UPDATE THE LAST ONE!!)
        res.extend([cnt, cur])

        return ''.join(map(str, res)) #return string


# use map() to convert each item in the list to a string, and then join them
#e.g.  ', '.join(map(str, list_of_ints))

solution = Solution()
print(solution.countAndSay(4))