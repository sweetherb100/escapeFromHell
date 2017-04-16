# performance : O(n log n), worst case : O(n^2)
# space complexity : O(n)
#
# 기본 아이디어 :
# Step 1]
# 1) pivot(마지막 원소)를 기준으로 맨 앞에 벽을 세워두고
# 2) pivot 보다 크면 벽 뒤, pivot 보다 작으면 벽과 swap 후 벽을 오른쪽으로 한칸 이동
# 3) 리스트를 한번 순회 마치면, pivot을 wall과 바꿔주고, wall을 pivot으로 return
#
# Step 2]
# 벽 기준 왼쪽 리스트, 오른쪽 리스트를 또 quick sort 진행


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
    #repeat until left item hit the end of list
    while left<pivot:
        #if left item is smaller than pivot, swap left item with wall and move wall to right
        if list[left]<list[pivot]: #3  4  8(wall)  7  5
            list[wall], list[left] =list[left],list[wall]
            wall = wall+1
        left=left+1
    #when left hit the end of list, swap pivot with wall
    # -> pivot이 wall을 중심으로 왼쪽은 pivot보다 작고, 오른쪽은 pivot보다 크므로
    list[wall],list[pivot]=list[pivot],list[wall]
    pivot=wall
    return pivot

list = [1, 2, 4, 6, 8, 13]
print(quickSort(list, 0,len(list)-1))

