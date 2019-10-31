'''
Reorganize String:
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  
If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""

*python
1) string.count(x)
2) extend
3) string.sort(reverse=True)
4) "".join(list)
'''


class Solution():
    def reorganizeString(self, string):
        n = len(string)
        info = []

        for x in set(string) :#range(len(strset)): #### WRONG!!!
            if string.count(x) > (n+1)//2: #valid only until the max count is <= (n+1)//2
                return ""

            info.append((string.count(x), x)) #####save as tuple
        info.sort(reverse=True) #descending order (default : ascending)

        infostr = []
        for i in range(len(info)):
            infostr.extend([info[i][1]] * info[i][0])

        #infostr : the largest repeating count for sure will be <= (N+1)//2
        result = [None] * n

        # jump by 2 starting from index 0
        result[::2] = infostr[: (n+1)//2] #using first (n+1)//2 elements, distribute to the result

        # jump by 2 starting from index 1
        result[1::2] = infostr[(n + 1) // 2:] #using the rest of elements starting from (n+1)//2, distribute to the result

        return "".join(result) ###result NO: return by string

sol=Solution()
print(sol.reorganizeString("aabc"))

print(set("aabc"))