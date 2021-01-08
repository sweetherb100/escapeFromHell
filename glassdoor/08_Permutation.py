'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example :
[1,1,2] have the following unique permutations:

[1,1,2]
[1,2,1]
[2,1,1]

number of permutation : n! 
*Recursion
1) Starting in front of index, swap with the rest if char
2) Excluding the swapped index, swap remained index with the rest of char

'''


### should be unique: use dict
### ''.join(map(str, A[::])): it is needed to change from list to string
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.result = []
        self.mem = {}

    def permute(self, A):
        # [1,2,3,4] : start with 1 and permute [2,3,4]
        #           start with 2 and permute [1,3,4]
        #           start with 3 and permute [1,2,4]
        # ...

        self.permute_helper(A, 0) #orig list, starting
        return self.result

    def permute_helper(self, A, start):
        # base condition : there is no interesting string behind
        if start == len(A): #reached the end
            temp = ''.join(map(str, A[::]))  #temp becomes string, ''.join(A[::]) doesnt work because it is number
            if temp not in self.mem: #mem: dict to keep track of the unique permutation
                self.mem[temp] = True  # save
                self.result.append(A[::])  # copy by value the list
                return

        # recursion
        for i in range(start, len(A)):
            A[start], A[i] = A[i], A[start]  # swap
            self.permute_helper(A, start + 1)
            A[start], A[i] = A[i], A[start]  # swap it back!

sol=Solution()
print(sol.permute([1,1,2]))

class Solution2():
    def __init__(self):
        self.result=[]

    def permute(self,nums):
        nums = list(nums) #needed or else, TypeError: 'str' object does not support item assignment
        self.permute_helper(nums, 0) #orig list, starting
        return self.result

    def permute_helper(self, nums, start):
        #base condition
        if start == len(nums): #reached the end
            temp=''.join(map(str, nums[::])) #make list into string
            self.result.append(temp)
            return

        #recursion
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start] #SWAP
            self.permute_helper(nums, start + 1) #as it goes into recursive, start changes!
            nums[start], nums[i] = nums[i], nums[start] #SWAP IT BACK (CHANGE IT BACK TO ORIGINAL)



sol=Solution2()
# list=sol.permute("abc")
# print(list)
# print(len(list))

list=sol.permute("abcd")
print(list)
print(len(list))






