'''
performance : O(n logn)
-> Divide  : O (log n), Compare and Combine : O(n)
space complexity : O(n)

*Process
1) Divide in half until unsorted list has only one element
2) Conquer (Recursive)
3) Compare divided element and Combine

*Python
1) len(alist)//2 : divde (not /)

'''

def mergesort(alist):

    #Step 1: Divide
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # Step 2 : Conquer
        mergesort(lefthalf)
        mergesort(righthalf)

        #Step 3 : Combine
        i=0
        j=0
        k=0

        while i <len(lefthalf) and j < len(righthalf) :
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else :
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    return alist

print(mergesort([6,2,4,1,3,7,5,8]))



