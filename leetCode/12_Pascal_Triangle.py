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
    def pascalTriangle(self, numRows):
        result=[[1]]

        # step1: build the initial structure (dummy value with 1)
        for i in range(numRows-1):
            templist =[1]*(i+2)
            result.append(templist)

        # step2: construct the element in the right way
        for i in range(2, numRows, 1): #starting from 2nd index
            for j in range(1, len(result[i])-1, 1): #except 0 index and the last index
                result[i][j] = result[i-1][j-1] + result[i-1][j]

        return result

solution = Solution()
print(solution.pascalTriangle(5))

'''
# personally, too complicated...
def pascalTriangle2(self, numRows):
    result = [[1]]  # initialize with [1]
    templist = []

    for i in range(numRows - 1):  # apply numRows-1 times more (already initialized with [1])
        templist = []

        for j in range(len(result[i]) - 1):  # because we will use j+1 index in the next line
            templist.append(result[i][j] + result[i][j + 1])

        templist.insert(0, 1)  # put 1 in the front, 1 in the end in the last moment
        templist.append(1)
        result.append(templist)
    return (result)
'''
