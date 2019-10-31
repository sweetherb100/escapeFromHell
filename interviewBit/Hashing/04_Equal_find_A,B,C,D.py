'''
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

Example:
Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)


Note:
1) Return the indices `A1 B1 C1 D1`, so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 

2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 
`'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        dict = {}
        indexlist = []
        sum = 0

        ### USE 2 FOR LOOPS AND DICT TO KEEP TRACK OF THE SUMS AND SAVE THAT SUM (COMPARE WITH HASH_02_2_SUM)
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)): # A1 < B1, C1 < D1
                sum = A[i] + A[j]
                if sum not in dict: #save old A + B
                    dict[sum] = [i, j] #save the index
                else: #if already in the sum, old A + B exists
                    if dict[sum][0] < i and dict[sum][1] != j and dict[sum][1] != i:
                        # A1 < C1, B1 != D1, B1 != C1
                        indexlist.append([dict[sum][0], dict[sum][1], i, j]) #save the index

        return min(indexlist)  # return min w.r.t. lexicographical order


solution = Solution()
print(solution.equal([3, 4, 7, 1, 2, 9, 8]))
#answer : [0, 2, 3, 5]


