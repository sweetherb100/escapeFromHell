"""Calculate the Greatest Common Divisor of a and b.

   Unless b==0, the result will have the same sign as b (so that when
   b is divided by it, the result comes out positive).
   """

#Euclidean algorithm to find GCD
def gcd(a, b):
    while b!= 0: #stop when b==0
        a, b = b, a%b #swap
    return a

print(gcd(36,24))