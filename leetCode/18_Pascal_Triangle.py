'''
Input: 5
Output:
[
     [1], :0
    [1,1], :1
   [1,2,1], :2
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        resultlist=[[1]]
        for i in range(1,numRows,1): #starting from 1~4
            templist=[1,1]
            if i==1:
                resultlist.append(templist)
            else: #starting from 2
                for i2 in range(i-1): #0,1
                    templist.insert(i2+1,resultlist[i-1][i2]+resultlist[i-1][i2+1])
                resultlist.append(templist)
        return resultlist

solution = Solution()
print(solution.generate(5))