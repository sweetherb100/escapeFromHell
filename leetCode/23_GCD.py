"""Calculate the Greatest Common Divisor of a and b.

   Unless b==0, the result will have the same sign as b 
   (so that when b is divided by it, the result comes out positive).
   """

#Euclidean algorithm to find GCD
class Solution:
    def gcd(self,a, b):
        while b!= 0: #stop when b==0
            print(a%b)
            a, b = b, a%b #swap
        return a

solution=Solution()
# print(solution.gcd(36,24))
print(solution.gcd(24,36)) #order doesn't matter I guess...
