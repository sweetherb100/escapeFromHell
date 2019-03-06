
class Solution(object):
    def secondLargest(self, list):

        if len(list) ==1 :
            print("no second largest")
        elif len(list) ==2:
            return min(list[0], list[1])

        maxnum=list[0]
        secondmaxnum=list[1]

        for i in range(2,len(list)): #can start from the 3rd element
            if maxnum < list[i] : #update max
                maxnum=list[i]
            elif  list[i] < maxnum and secondmaxnum < list[i]:
                secondmaxnum=list[i] #update secondmax

        return secondmaxnum


solution = Solution()
print(solution.secondLargest([7,1,5,3,6,4]))
