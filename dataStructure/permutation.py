'''
Permutation
*Idea (use Recursion)
1) Starting in front of index, swap with the rest if char
2) Excluding the swapped index, swap remained index with the rest of char
'''

def permute(nums):
    def backtrack(start, end): #needed to be defined in front
        if start == end:
            ans.append(nums[:]) #WHY DOESNT NUMS WORK???

        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1, end) #as it goes into recursive, start changes!
            nums[start], nums[i] = nums[i], nums[start] #swap it back to make into original

    nums=list(nums)
    ans = []
    backtrack(0, len(nums))
    return ans


print(permute("abcd"))
# print(permute(["a","b","c"]))




