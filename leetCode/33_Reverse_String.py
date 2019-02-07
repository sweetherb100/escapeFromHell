'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """

        # O(1) extra memory

        length = len(s)

        for i in range(len(s) // 2): ### BE CAREFUL!! Should be len(s)//2!
            print(s[i])
            print(s[length - 1 - i])
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]  # swap
