'''
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence  is different


N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1
'''
import math


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        length = int(math.log10(A)) + 1
        tot_comb = length * (length + 1) / 2

        hashset = set()
        numarr = self.getDigitArray(A, [])
        temp = 0

        for i in range(len(numarr)):
            temp = numarr[i]
            hashset.add(temp)
            for j in range(i + 1, len(numarr)):
                temp *= numarr[j]
                hashset.add(temp)

        if tot_comb != len(hashset):
            return 0
        else:
            return 1

    def getDigitArray(self, n, list):
        if 0 <= n and n <= 9:  # if 1 digit
            list.append(n)
            return list

        else:
            self.getDigitArray(n // 10, list)
            list.append(n % 10)
            return list


