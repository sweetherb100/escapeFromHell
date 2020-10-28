'''
Write a function that reverses a string. 
The input string is given as an 'array' of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution(object):
    def reverseString(self, s):
        length = len(s) # space complexity: O(1)

        # swap the front and the end and iterate only half of the array length
        for i in range(len(s) // 2): ### BE CAREFUL!! Should be len(s)//2!
            s[i], s[length-1 - i] = s[length-1 - i], s[i]  # swap, BE CAREFUL!! index should e length-1

        return s


sl=Solution()
print(sl.reverseString(['a','b','c','d']))

# ss="abcd"
# ss[0] = 'f'
# print(ss) # 'str' object does not support item assignment