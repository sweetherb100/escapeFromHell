'''
Data structure : vector (each element indicates the flag)
(instead of 2 for loop)

In a more smarter way, I don't need to find each prime!
I just need to find the number of prime
'''


class Solution(object):
    def countPrimes(self, n):
        vect=[1]*(n+1) #for simplicity, vector size n+1

        vect[0]= 0
        vect[1]= 0 #not prime

        if n <=1:
            return 0

        #1 for loop : complexity O(n/2)
        for i in range(2, n//2+1): #in theory, check until 10/2= 5; put until "n//2+1"
            if vect[i] == 1:
                vect[2*i:n+1:i] = [0] * len(vect[2*i:n+1:i]) #n+1 means: only until n

        #if 1, prime; if not, not prime
        print(vect)
        return(sum(vect))

solution = Solution()
print(solution.countPrimes(10))

#list2=[1,2,3,4,5,6,7]
#print(list2[1:7:2]) #[2, 4, 6]


'''
        2 for loops Complexity : O(n^2)
        
        primelist = []
        if n <= 1:
            return 0  # no prime number

        primelist.append(2)  # intial value

        for i in range(3, n):
            for j in range(2, i): #not i-1 because it is already excluded
                if i % j == 0: # i= 6, j= 2,3,4,5
                    break
                if j== i-1 : #arrived to the last
                    primelist.append(i)

        print(primelist)
        return len(primelist)

'''