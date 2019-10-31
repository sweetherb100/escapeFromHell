'''
Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3]

https://www.youtube.com/watch?v=VNbkzsnllsU
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = [0] #saving index
        A = [-1] + A
        A.append(-1)
        max_area = 0

        for i in range(1, len(A)): #starting from 1
            print(stack)
            print(A)
            print(A[i])
            print(A[stack[-1]])
            print("**********")
            while A[i] < A[stack[-1]]: #current value is smaller
                h = A[stack.pop()]
                area = h * (i - 1 - stack[-1])
                if area > max_area:
                    max_area = area
                print(max_area)
                print("###########")
            stack.append(i) #append visited index

        return max_area

solution = Solution()
# print(solution.largestRectangleArea([ 2, 82, 11, 89, 7, 21, 92, 13, 11, 94, 4, 96, 3 ]))
print(solution.largestRectangleArea([2,1,5,6,2,3]))



'''
# PARTIALLY CORRECT
    # I DIDNT USE STACK/QUEUE BUT I USED 2 FOR LOOP
    # EXTRA CONSIDERATION : ONE HEIGHT CAN BE MAX!
    def largestRectangleArea2(self, A):
        #Exception
        if len(A) == 0:
            return 0
        elif len(A) == 1:
            return A[0]

        area = 0
        minheight = 0

        for i in range(len(A) - 1): # I will use index i+1
            if A[i] > area: # EXTRA CONSIDERATION : ONE HEIGHT CAN BE MAX!
                area= A[i]

            for j in range(i + 1, len(A)):
                if j == i + 1:
                    minheight = min(A[i], A[j])
                else:
                    minheight = min(minheight, A[j])

                if (j - i + 1) * minheight > area: #width is 1 so I shouldn't just do j-i
                    area = (j - i + 1) * minheight
        return area

'''