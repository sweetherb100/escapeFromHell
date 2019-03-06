class Solution():
    def convertToInteger(self, str):
        n=len(str)
        result = 0

        for i in range(len(str)):
            result += int(str[i])*pow(10, n-1-i) #at some point, I have to use int

        return result

sol = Solution()
print(sol.convertToInteger("123"))