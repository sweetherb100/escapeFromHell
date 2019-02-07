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
        result = [[1]]
        templist=[]

        for i in range(numRows-1):
            templist = []

            for j in range(len(result[i])-1):
                templist.append(result[i][j]+result[i][j+1])
            templist.insert(0,1) #put 1 in the front, 1 in the end in the last moment
            templist.append(1)

            result.append(templist)

        return (result)

solution = Solution()
print(solution.generate(5))

'''
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # initialize
        result = [[1]]
        if numRows == 0:
            return result
        if numRows == 1:
            result.append([1, 1])
            return result

        result.append([1, 1])
        for i in range(2, numRows, 1):
            tempresult = [1]
            for j in range(len(result[i - 1]) - 1):
                tempresult.append(result[i - 1][j] + result[i - 1][j + 1])
            tempresult.append(1)  # the last 1
            result.append(tempresult)

        return (result)
'''