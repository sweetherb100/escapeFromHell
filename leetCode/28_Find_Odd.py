'''
Find element that has the odd number of count

Example:
2 : total 4 count
7 : total 2 count
6 : total 2 count
3: total 1 count

Output: 3
'''

# strategy: Switch on and off. Use Hashmap data structure.

class Solution(object):
    def findodd(self, list):
        dict = {}

        # going through the array
        for i in range(len(list)):
            if list[i] not in dict:
                dict[list[i]] = 1
            else : #visited again
                dict[list[i]] = dict[list[i]]*(-1) #change the sign

        for key, value in dict.items():
            if value == 1:
                return key


solution = Solution()
print(solution.findodd([2, 7, 6, 3, 2, 2, 2, 7, 6]))