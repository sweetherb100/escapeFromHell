'''
performance : O(n^2)
space complexity : O(1) (don't need extra space but in-place)
swapping : N-1 (i for loop)

'''

def bubblesort(alist) :
    for i in range(len(alist) -1):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1]  = alist[j+1], alist[j]
    return alist

print(bubblesort([4,6,1,3,5,2,0,3523,1,326]))
