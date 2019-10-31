'''
Implement int sqrt(int x).
Compute and return the square root of x.
If x is not a perfect square, return floor(sqrt(x))

Example :
Input : 11
Output : 3
'''

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        # Exception:
        if A == 0:
            return 0
        elif A == 1:
            return 1

        start = 1  # NOT 0
        end = A  # NOT A-1

        while start <= end: #ALWAYS FOR B.S
            mid = (start + end) // 2 #ALWAYS FOR B.S

            if mid*mid <= A and (mid+1)*(mid+1) > A: #WRONG SYNTAX : mid^2
                return mid

            elif mid*mid > A:  # on the left
                end = mid - 1

            elif mid*mid < A:  # on the right (specify as much as possible just in case)
                start = mid + 1

solution = Solution()
print(solution.sqrt(6))
