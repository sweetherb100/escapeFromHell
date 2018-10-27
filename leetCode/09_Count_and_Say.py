'''
The
count and say sequence is the sequence of integers with the first five terms as following:

1. 1
2. 11
3. 21
4. 1211
5. 111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count - and -say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"
Example 2:
Input: 4
Output: "1211"
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num_str="1"
        for i in range(1,n,1):
            num_str=solve(num_str)
            print(str(i) + " : " + num_str)

        return num_str


def solve(num_str):
    new_str=""
    start_pos =0
    while start_pos < len(num_str):
        length=get_length(num_str[start_pos:]) #duplicate length from start_pos
        new_str += str(length) + num_str[start_pos]
        start_pos+= length #jump as much as length of duplicate
    return new_str

def get_length(num_str):
    first_char= num_str[0]
    for i in range(len(num_str)):
        if num_str[i] != first_char:
            return i #actually this is length

    return len(num_str)


solution = Solution()
print(solution.countAndSay(5))