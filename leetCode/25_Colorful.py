'''
For Given Number N find if its COLORFUL number or not (return 0/1)

COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product(multiplication) of every digit of a contiguous subsequence is different


Example:
N = 23

contiguous sub-subsequence: 2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 
Output : 1
'''

class Solution:
    # @param A : integer
    # @return an integer
    def getDigitArray(self, n, list):
        if 0 <= n and n <= 9:  # if 1 digit
            list.append(n)
            return list

        else:
            self.getDigitArray(n // 10, list)
            list.append(n % 10)
            return list


    def colorful(self, A):
        numarr = self.getDigitArray(A, []) #each digit of the integer
        length = len(numarr)
        tot_comb = length * (length + 1) / 2

        hashset = set()

        #going through each digit element
        for i in range(length):
            temp = numarr[i] #reset temp
            hashset.add(temp)
            for j in range(i+1, length):
                temp *= numarr[j] #32, 324, 3245
                hashset.add(temp)

        if tot_comb != len(hashset): #exist multiplication that are the same
            return 0
        else:
            return 1


solution = Solution()
print(solution.colorful(23))
print(solution.colorful(3245))

