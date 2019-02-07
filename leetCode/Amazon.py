### Use c! Don't just use them to compare!
### Use other data structure

list=[1, 3, 2, 5, 6, 7, 12]

class Solution(object):
    def findc(self, list, c):
        visited=[]
        visited.append(list[0])

        for i in range(1,len(list),1):
            if c-list[i] in visited:
                return True
            else:
                visited.append(list[i])

        return False

solution = Solution()
print(solution.findc([1, 3, 2, 5, 6, 7, 12],222))


'''
def exercise(list,c):
    for i in range(len(list)):
        for j in range(i+1, len(list),1):
            if list[i]+list[j] == c:
                return True
    
    return False
'''

