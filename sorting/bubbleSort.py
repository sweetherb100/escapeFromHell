# performance : O(n^2)
# space complexity : O(1)
# swapping : N - 1번 (보통 i for loop)
#
# 참고 (헷갈렸음)
# list =[i for i in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 0부터 시작, 10 미만

def bubblesort(alist) :
    for i in range(len(alist) -1): #i는 swap 되는 횟수
        #github에서는 range(len(alist)-1)로만 되어있는데
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1]  = alist[j+1], alist[j]
    return alist

print(bubblesort([4,6,1,3,5,2,0,3523,1,326]))
