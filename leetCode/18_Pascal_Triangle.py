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

solution = Solution()
print(solution.generate(5))

'''
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
'''