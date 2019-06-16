'''
Return True if there are 2 elements which sum to input c
Return False if not
'''


class Solution(object):
    def findc(self, list, c):
        visited=[]
        visited.append(list[0])

        # Use 1 for loop
        for i in range(1,len(list),1):
            if c-list[i] in visited:  # visited(old) + list[i](new) = c
                return True
            else:
                visited.append(list[i])

        return False

solution = Solution()
print(solution.findc([1, 3, 2, 5, 6, 7, 12], 222))
print(solution.findc([1, 3, 2, 5, 6, 7, 12], 19))


'''
NOT RECOMMENDED!! (2 for loop)

def exercise(list,c):
    for i in range(len(list)):
        for j in range(i+1, len(list), 1):
            if list[i]+list[j] == c:
                return True
    
    return False
'''

