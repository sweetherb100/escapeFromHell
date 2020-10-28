#recursive
# if clause: only take care of the base expression (last part)

class Solution:
    def getDigitArray(self, n, list):
        if 0 <= n and n <= 9:  # if 1 digit
            print(n)
            list.append(n)
            return list

        else:
            self.getDigitArray(n // 10, list)
            list.append(n % 10) #append the remainder in the end
            return list


solution = Solution()
print(solution.getDigitArray(2356,[]))