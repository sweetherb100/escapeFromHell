# performance : O(n logn)
# -> 반으로 쪼개는 과정 : O (log n), 비교하여 합치는 과정 : O(n)
# space complexity : O(n)
#
# Step 1 : 정렬되어 있지 않은 리스트를 하나의 원소가 남을 때까지 반씩 쪼개기 (Divide)
#  Step 2 : 재귀함수 (Conquer)
# Step 3 : 쪼개어진 값을 비교를 하여 정렬된 아이템으로 병합 (Combine)

def mergesort(alist):

    #Step 1: Devide
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



