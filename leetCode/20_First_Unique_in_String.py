'''
I should return the element that is not-repeated but also the first one if there are multiple
=> Since there is an order that I should think of, let's approach with vector together with hashmap
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ####  find first non-repeating character (so the order is important)
        dict = {}
        visited = []

        # going through the string element
        for i in range(len(s)):
            if s[i] not in dict: #access in hashmap : O(1)
                dict[s[i]] = True  # key: element, value: unique (boolean)
                visited.append(i) #save the index
            else:  # more than 2
                dict[s[i]] = False  # not-unique (boolean)


        # going through the visited element
        for i in range(len(visited)):
            if dict[s[i]] == True: #unique
                return s[i]

        return -1 #no unique string

solution = Solution()
print(solution.firstUniqChar("geeksforgeeks"))
