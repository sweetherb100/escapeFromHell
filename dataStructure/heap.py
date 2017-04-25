'''
*Performance : O(n log n)
O(1) for get root value(max, min value)

*Heapsort : in-place algorithm (doesn't need extra space)

*Heap Tree : parent node is bigger than the child node (or smaller)
(not only the root but also for each sub tree)

*Heapsort Idea :
1) use Array as a data structure of heap tree 
cf) Binary Search Tree : really implement tree structure

2) BAD : traverse first to the end node and change the value
BETTER  : traverse first to the LAST NODE WHICH HAS CHILDREN and change the value (twice better permance)
(size//2) -1 : LAST NODE WHICH HAS CHILDREN INDEX

3) Step 1: heapify (transform tree-> heap tree)
2*i + 1 : LEFT CHILD NODE
2*i + 2 : RIGHT CHILD NODE
Step 2: siftdown (compare parent, left, right and swap the biggest to parent. Then go recursive)
Step 3 : After making heap tree, do heap sort
'''

def Heapsort(a):
    def heapify(a,size):
        p = (size//2) -1 #LAST NODE WHICH HAS CHILDREN INDEX
        while p>=0:
            siftdown(a,p,size)
            p-=1

    def siftdown(a,i,size):
        l=2*i +1 #LEFT CHILD NODE
        r=2*i +2 #RIGHT CHILD NODE
        largest = i
        if l<=size-1 and a[l]>a[i]:
            largest = l
        if r<=size-1 and a[r] > a[largest]:
            largest=r
        if largest !=i:
            a[i],a[largest] = a[largest],a[i] #swap
            siftdown(a,largest,size) #to make child subtree heap tree structure

    size=len(a)
    heapify(a,size)

    end=size-1
    while(end>0):
        a[0], a[end] = a[end], a[0] #swap #put the biggest element at the end of the list
        siftdown(a,0,end) #heapify from index 0 to end (first loop : size-1. already excluded the end node which its swapping finished)
        end-=1


arr=[2,3,1,4,10,7]
Heapsort(arr)
print(arr)