# O(n log n)
# O(1) for get root value(max, min value)
# Heapsort : in-place algorithm (별도의 space 필요하지 않음)
# Heap Tree
# 1) max Heap Tree (root가 가장 큰 값일 때)
# 2) min Heap Tree (root가 가장 작은 값일 때)
# Heap 특성 : parent가 자식보다 클 때 (혹은 작을 때)


#use Array as a data structure of heap tree
def Heapsort(a):
    #기본 아이디어 : 노드를 순회하면서 치환해주면 되는데, 그러면 퍼포먼스가 매우 떨어짐
    def heapify(a,size): #일반 트리 -> heap tree로 변환
        p = (size//2) -1 #자식이 있는 마지막 노드 index (여기서부터 보면 퍼포먼스 2배)
        while p>=0:
            siftdown(a,p,size)
            p-=1

    def siftdown(a,i,size):
        l=2*i +1 #left child node
        r=2*i +2 #right child node
        largest = i
        if l<=size-1 and a[l]>a[i]:
            largest = l
        if r<=size-1 and a[r] > a[largest]:
            largest=r
        if largest !=i:
            swap(a,i,largest)
            siftdown(a,largest,size) #자식 부트리가 계속 heap tree 유지 하기 위해서

    def swap(a,i,j):
        tmp=a[i]
        a[i]=a[j]
        a[j]=tmp

    size=len(a)
    heapify(a,size)

    #heap tree로 만든 상태에서 heap Sort (ascending order)
    #example로 보면서 이해하기
    end=size-1
    while(end>0):
        swap(a,0,end) #가장 마지막 노드에 제일 큰 값을 넣는다.
        siftdown(a,0,end) #heapify (swapping이 끝나서 배제된 끝부분 노드는 제외)
        end-=1


arr=[1,3,2,4,9,7]
Heapsort(arr)
print(arr)

#참고사이트
# https://github.com/minsuk-heo/problemsolving/blob/master/sort/HeapSort.py