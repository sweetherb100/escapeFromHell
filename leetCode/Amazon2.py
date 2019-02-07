#Find odd number of number: switching on and off!
# 2 : total 4,
# 7 : total 2,
# 6 : total 2,
# 3: total 1 (I should find this!)

### Use other data structure
### how to use dictionary : "items()"


class Solution(object):
    def findodd(self, list):
        dict = {} #initialize

        for i in range(len(list)):
            if list[i] not in dict:
                dict[list[i]] = 1
            else :
                dict[list[i]] = dict[list[i]]*(-1)

        print(dict)

        for key, value in dict.items():
            if value == 1:
                return key


solution = Solution()
print(solution.findodd([2, 7, 6, 3, 2, 2, 2, 7, 6]))
#result 3