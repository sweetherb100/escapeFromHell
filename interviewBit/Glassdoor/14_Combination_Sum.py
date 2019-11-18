'''
Given a set of candidate numbers (C) and a target number (T), 
find all "unique" combinations in C where the candidate numbers sums to T.

*Be careful: the candidate number doesn't necessarily be used once but can be used more than once!
https://www.youtube.com/watch?v=Viu3iQLmQlY

Time Complexity :
O( C(n,1) + C(n,2) + ... C(n,p))
Space Complexity:
O(path + recursion stack) 
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def __init__(self):
        self.result = []
        self.mem = {}

    def combinationSum(self, ls, target):
        ls.sort()  # sort first, [2,3,6,7], target 7
        self.combi_helper(ls, target, 0, [])
        return self.result

    def combi_helper(self, ls, target, start, path):
        # base condition
        if target == 0 and ''.join(map(str, path[::])) not in self.mem: #use map(str, ) because path is number
            self.mem[''.join(map(str, path[::]))] = True
            self.result.append(path[::])  # copy by value the list
            return

        # this shouldnt be base condition because I shouldnt run the rest of for loop (not just this)
        # if ls[start] > target:
        #     return

        for i in range(start, len(ls)):
            if ls[i] > target:
                break  # dont need to proceed the rest of for loop
                        #also dont even need to append on my path

            path.append(ls[i])
            self.combi_helper(ls, target - ls[i], i, path)
            path.pop() #to append the next for loop element, I need to pop the previous ls[i]



sol=Solution()
print(sol.combinationSum([2,3,6,7],7))
# [[2, 2, 3], [7]]