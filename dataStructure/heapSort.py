'''
*Performance
1) O(n log n)
2) O(1) for get root value(max, min value)

*Heapsort : in-place algorithm (doesn't need extra space)

*Heap Tree : parent node is bigger than the child node (or smaller)
(not only the root but also for each sub tree)

*Heapsort Idea :
1) use Array as a data structure of heap tree 
cf) Binary Search Tree : really implement tree structure

2) BAD IMPLEMENTATION : traverse first to the end node and change the value
BETTER IMPLEMENTATION  : traverse first to the LAST NODE WHICH HAS CHILDREN and change the value (twice better performance)
(size//2) -1 : LAST NODE WHICH HAS CHILDREN INDEX

3) heapify (transform tree-> heap tree)
Step 1: 
2*i + 1 : LEFT CHILD NODE
2*i + 2 : RIGHT CHILD NODE
Step 2: 
shiftdown (compare parent, left, right and swap the biggest to parent. Then go recursive)
Step 3 : 
After making heap tree, do heap sort
'''

#max heap (put the largest value on the root)
def Heapsort(list):
    def heapify(list,size):
        pos = (size//2) -1 #LAST NODE WHICH HAS CHILDREN INDEX
        while pos>=0:
            shiftdown(list,pos,size)
            pos -= 1 #move closer to root in while loop

    def shiftdown(list,i,size):
        l=2*i +1 #LEFT CHILD NODE
        r=2*i +2 #RIGHT CHILD NODE
        largest = i
        if l<=size-1 and list[l]>list[i]:
            largest = l
        if r<=size-1 and list[r] > list[largest]:
            largest=r

        # option for largest is either left child or right child!
        if largest !=i:
            list[i],list[largest] = list[largest],list[i] #swap
            shiftdown(list,largest,size) #to make child subtree heap tree structure

    size=len(list)
    heapify(list,size)
    print(list) #[10, 4, 7, 2, 3, 1]

    end=size-1
    while end>0:
        list[0], list[end] = list[end], list[0] #swap #put the biggest element at the end of the list
        shiftdown(list,0,end) #shiftdown from index 0 of length end; shiftdown(list,i,size)
                            # don't need to call heapify because while loop itself plays a role as heapify
        end-=1


list=[2,3,1,4,10,7]
Heapsort(list)
print(list) #[1, 2, 3, 4, 7, 10]
