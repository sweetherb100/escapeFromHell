class Solution(object):
    def secondLargest(self, list):

        if len(list) == 1:
            print("no second largest")
            return list[0]
        elif len(list) == 2:
            return min(list[0], list[1])

        maxnum=list[0]
        secondmaxnum=list[1]

        # use 1 for loop
        # Time comlexity O(N)
        # Space complexity O(k), k: kth largest

        # Can start from the 3rd element
        for i in range(2,len(list)):
            if maxnum < list[i] : #update max
                maxnum=list[i]
            elif  list[i] < maxnum and secondmaxnum < list[i]: #update secondmax
                secondmaxnum=list[i]
        return secondmaxnum

solution = Solution()
print(solution.secondLargest([7,1,5,3,6,4]))
