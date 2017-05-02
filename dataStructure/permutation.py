'''
Permutation
*Idea (use Recursion)
1) Starting in front of index, swap with the rest if char
2) Excluding the swapped index, swap remained index with the rest of char
'''

def perm(n,i):
    if i == len(n) -1:
        print(n)
    else:
        for j in range(i,len(n)): #i<=j<len(n)
            n[i],n[j] = n[j],n[i]
            perm(n,i+1)
            n[i],n[j] = n[j],n[i] #swap back, for the next loop

perm([1,2,3],0)

# print([j for j in range(0,10)])



