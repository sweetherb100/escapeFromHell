'''
*When Queue is used?
1) Print job queue
2) BFS (Breadth First Search)

*Outline :
1) enqueue(insert(0,item)), dequeue(pop) methods

*Python
1) list.pop(0) : pop the first element of list
'''

class Queue:

    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()

    def print_queue(self):
        print(self.items)

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue() #[3,2,1]
queue.dequeue()
queue.print_queue() #[3,2]
print(queue.is_empty())
print(queue.size())
