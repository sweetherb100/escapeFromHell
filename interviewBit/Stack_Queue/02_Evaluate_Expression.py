'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''


### use STACK to save numbers!
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        # in principle, in stack, there should be only 2 numbers to be evaluated
        stack = []
        for i in range(len(A)):
            if A[i] == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                val = val1 + val2
                stack.append(val) #push also that number

            elif A[i] == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                val = val2 - val1 ### BE CAREFUL WITH THE ORDER
                stack.append(val) #push also that number

            elif A[i] == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                val = val1 * val2
                stack.append(val) #push also that number

            elif A[i] == "/":
                val1 = stack.pop() #5
                val2 = stack.pop() #13
                val = val2 // val1 ### BE CAREFUL WITH THE ORDER AND USE //
                stack.append(val) #push also that number

            else: # push the numbers
                stack.append(int(A[i]))

        return stack.pop()

solution = Solution()
print(solution.evalRPN([ "4", "13", "5", "/", "+" ]))





