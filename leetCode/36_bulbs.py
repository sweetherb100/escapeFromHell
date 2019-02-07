class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):

        count = 0
        for i in range(len(A)):
            if A[i] == 0:
                A[i] = 1
                count += 1
                for j in range(i + 1, len(A)):
                    A[j] = abs(A[j] - 1)
                    # A[i+1:len(A)] = abs(A[i+1:len(A)] - [1]*len(A[i+1:len(A)]) ) CANNOT SUBTRACT USING 2 LISTS

        return count