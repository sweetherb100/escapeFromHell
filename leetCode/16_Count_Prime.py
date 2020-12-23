'''
Data structure : vector (each element indicates the flag)

In a more smarter way, I don't need to find each prime!
I just need to find the number of prime
'''

class Solution(object):
    def countPrimes(self, n):
        # Exception
        if n <=1:
            return 0

        #step1: create a vector as the length of n
        vect=[1]*(n+1) #for simplicity, vector size n+1

        # Initialize
        vect[0]= 0
        vect[1]= 0 #not prime

        #Complexity O(n/2)
        #step2: going through half of n iteration
        for i in range(2, n//2+1): #in theory, check until 10/2= 5; put until "n//2+1"
            if vect[i] == 1:
                # step3: update as 0 for the multiples of index i
                vect[2*i:n+1:i] = [0] * len(vect[2*i:n+1:i]) #n+1 means: only until n

        #if 1, prime; if not, not prime
        print(vect)
        return(sum(vect))


solution = Solution()
print(solution.countPrimes(6))

# list2=[0,1,2,3,4,5,6,7]
# print(list2[2:7:2])
#[2, 4, 6]
