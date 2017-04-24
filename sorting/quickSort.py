'''
performance : O(n log n), worst case : O(n^2)
space complexity : O(n)
Divide-Conquer (divide-conquer(recursive)-combine)

*Outline :
[Step 1]
1) put the wall in front and set the last element as pivot
2) If pivot is bigger than element, swap element with the wall and move the wall one right.
3) After going through list, swap pivot and wall and return wall as pivot

[Step 2]
Quick sort left list, right list respectively
'''

def quickSort(list,start,end):
    if start<end:
        pivot = partition(list,start,end)
        quickSort(list,start,pivot-1)
        quickSort(list,pivot+1,end)
    return list

def partition(list,start,end):
    pivot=end
    wall=start
    left=start
    while left<pivot: #repeat until left item hit the end of list
        #if pivot item is bigger than element, swap left item with wall and move wall to right
        if list[left]<list[pivot]:
            list[wall], list[left] =list[left],list[wall]
            wall = wall+1
        left=left+1
    #when left hit the end of list, swap pivot with wall
    #left part of wall is smaller than pivot, and right part of wall is bigger than pivot.
    list[wall],list[pivot]=list[pivot],list[wall]
    pivot=wall
    return pivot

list = [4,6,5,1,2,3]
print(quickSort(list, 0,len(list)-1))

