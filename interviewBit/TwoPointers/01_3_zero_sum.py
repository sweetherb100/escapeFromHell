'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all "unique" triplets in the array which gives the sum of zero.
'''

####### HOW TO GET UNIQUE LIST: can directly compare with :
# if [A[i], A[startpos], A[endpos]] not in result:

class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    def threeSum(self, A):
        A.sort()  # O(n^2)
        result = []

        for i in range(len(A) - 2):
            startpos = i + 1 #startpos should be always after i
            endpos = len(A) - 1

            while (startpos < endpos):
                if (A[i] + A[startpos] + A[endpos] == 0):  # FOUND
                    if [A[i], A[startpos], A[endpos]] not in result:
                        result.append([A[i], A[startpos], A[endpos]])
                    startpos += 1 #update
                    endpos -= 1 #update


                elif (A[i] + A[startpos] + A[endpos] < 0):  # should be increased!
                    startpos += 1  # update

                elif (A[i] + A[startpos] + A[endpos] > 0):  # should be decreased!!
                    endpos -= 1  # update

        return result #[::-1]




solution = Solution()
print(solution.threeSum([ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]))
#[-5 0 5 ] [-5 1 4 ] [-4 -1 5 ] [-4 0 4 ] [-4 1 3 ] [-3 -2 5 ] [-3 -1 4 ] [-3 0 3 ] [-2 -1 3 ] [-2 1 1 ] [-1 0 1 ] [0 0 0 ]

A=[ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
A.sort()
print(A)
#[-5, -4, -4, -4, -3, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 3, 4, 4, 5]
