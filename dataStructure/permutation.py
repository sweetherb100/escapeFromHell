# permutation
# 기본 아이디어 (Recursion 이용) :
# 1) 앞의 index부터 시작하여 나머지 char와 swapping한다
# 2) swapping이 마친 앞의 index는 제외하고, 또 남아있는 문자열의 앞의 index부터
# 시작하여 나머지 char와 swapping 한다.

def perm(n,i):
    if i == len(n) -1:
        print(n)
    else:
        for j in range(i,len(n)): #i<=j<=len(n)
            n[i],n[j] = n[j],n[i]
            perm(n,i+1)
            n[i],n[j] = n[j],n[i] #swap back, for the next loop

perm([1,2,3],0)



