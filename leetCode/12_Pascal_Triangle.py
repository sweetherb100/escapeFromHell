'''
Input: 5
Output:
[
     [1], :0
    [1,1], :1
   [1,2,1], :2
  [1,3,3,1], :3
 [1,4,6,4,1] :4
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]] #initialize with [1]
        templist=[]

        for i in range(numRows-1): #apply numRows-1 times more (already initialized with [1])
            templist = []

            for j in range(len(result[i])-1): #because we will use j+1 index in the next line
                templist.append(result[i][j]+result[i][j+1])

            templist.insert(0,1) #put 1 in the front, 1 in the end in the last moment
            templist.append(1)
            result.append(templist)

        return (result)

solution = Solution()
print(solution.generate(5))
