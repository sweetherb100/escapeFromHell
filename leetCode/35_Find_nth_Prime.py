#prime: 2, 3, 5, 7, 11, 13, 17, 19, 23, ,...
class Solution(object):
    def findNthPrime(self, nth):
        i=0
        num=2

        while(i != nth) : #stop when i==nth
            if (self.isPrime(num)): #use isPrime function
                i+=1

            if (i == nth):
                return num

            num+=1


    def isPrime(self, num):
        for i in range(2,num,1): #if num==2, range(2,2,1), so will not go through the loop
            if num%i == 0:
                return False

        return True

solution = Solution()
print(solution.findNthPrime(9))

