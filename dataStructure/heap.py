'''
*Heap Tree : 
1) parent node is bigger than the child node (or smaller)
(not only the root but also for each sub tree)

2) use Array as a data structure of heap tree 
cf) Binary Search Tree : really implement tree structure

3) Different from heap Sort algorithm:
Heap Sort: make heap data structure of given array (within heapify, there is shiftdown)
Heap add/remove : each time add/remove item
shift_up(one time using while) and shift_down(recursively for the subtree)

http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/heap-delete.html
'''


# max heap
class Heap:
    def __init__(self):
        self.heap=[]
        self.size=0 #error if len(self.heap)

    def lefti(self, i):
        return 2*i +1 #LEFT CHILD NODE

    def righti(self, i):
        return 2 * i + 2  # RIGHT CHILD NODE

    def parenti(self, i):
        return (i+1)//2 -1

    def search(self, item):
        return item in self.heap

    def shift_up(self, idx):
        while idx > 0 and self.heap[idx]  > self.heap[self.parenti(idx)]:
            self.heap[idx], self.heap[self.parenti(idx)] = self.heap[self.parenti(idx)], self.heap[idx] #SWAP
            idx = self.parenti(idx)


    #Complexity : O(log n), shift_up
    def add(self, item):
        self.heap.append(item)
        self.size += 1

        #after adding in the last index and updating size, shift_up for that one item
        idx = self.size-1
        self.shift_up(idx)

    def remove(self, item):
        if item not in self.heap:
            print("doesn't exist the item")
            return False
        else:
            idx = self.heap.index(item)
            self.heap[idx]=self.heap[-1]
            self.heap.pop() #remove the last node and make it as "complete binary tree"
            self.size -= 1

            #from idx, shift_down recursively
            self.shift_down(self.heap, idx)


    def shift_down(self, list, i):
        l = self.lefti(i)
        r = self.righti(i)
        size = self.size
        largest = i


        if l <= size - 1 and list[l] > list[i]:
            largest = l
        if r <= size - 1 and list[r] > list[largest]:
            largest = r

        #largest can be either left child or right child
        if largest != i:
            list[i], list[largest] = list[largest], list[i]  # swap
            self.shift_down(list, largest)  # to make child subtree heap tree structure


heap = Heap()
heap.add(3)
heap.add(5)
heap.add(1)
heap.add(19)
heap.add(11)
heap.add(22)
print(heap.heap) #[22, 11, 19, 3, 5, 1]
heap.remove(22)
print(heap.heap)
print(heap.search(3))
