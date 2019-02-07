class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # find first non-repeating character (so the order is important)

        dict = {}
        visited = []

        for i in range(len(s)):
            if s[i] not in dict: #access in hashmap : O(1)
                dict[s[i]] = i  # save index
                visited.append(i)
            else:  # more than 2
                dict[s[i]] = -1  # cannot use 0 because 0 can be also the index

        print(visited)

        for i in range(len(visited)):
            print(dict[s[i]])
            if dict[s[i]] != -1:
                return i

        return -1
