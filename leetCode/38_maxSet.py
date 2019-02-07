'''
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        # negative num plays as partition

        dict = {}
        temp = 0
        templist = []
        for i in range(len(A)):
            if A[i] >= 0:
                temp += A[i]
                templist.append(A[i])
            else:
                dict[temp] = templist
                temp = 0
                templist = []  # reset

        max = -1  # can't be minus
        for key in dict.keys():
            if max < key:
                max = key

        return dict[key]
    

'''
# negative num plays as partition
    # minimum starting index : order is important!!!
    
        maxsum=-1
        maxlist=[]
        
        tempsum=0
        templist=[]
        
        for i in range(len(A)):
            if A[i] >= 0:
                tempsum+=A[i]
                templist.append(A[i])
                
            elif A[i] < 0:
                if tempsum > maxsum:
                    maxsum=tempsum
                    maxlist=templist
                tempsum=0
                templist=[] #reset
                
        if tempsum > maxsum:
            maxsum=tempsum
            maxlist=templist
        
        return maxlist
    
'''