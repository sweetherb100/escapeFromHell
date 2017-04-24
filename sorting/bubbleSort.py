'''
performance : O(n^2)
space complexity : O(1)
swapping : N-1 (i for loop)

*Python
1) list =[i for i in range(10)]
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

def bubblesort(alist) :
    for i in range(len(alist) -1): #number of swapping
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1]  = alist[j+1], alist[j]
    return alist

print(bubblesort([4,6,1,3,5,2,0,3523,1,326]))
