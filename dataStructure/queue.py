# queue는 언제 사용하느냐?
# 1) Print job queue
# 2) BFS (Breadth First Search)
#----------
#  -> -> ->
#----------
class Queue:

    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)
        #리스트 맨 앞에 새 요소 추가

    def dequeue(self):
        self.items.pop()
        #맨 마지막 요소 제거

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
queue.print_queue()
#[3,2,1]
queue.dequeue()
queue.print_queue()
#[3,2]
print(queue.is_empty())
print(queue.size())

#Python 메소드 정리
# list.insert(0,A) : list 맨 앞에 새 요소 추가
# list.append(A) : list 맨 뒤에 새 요소 추가
# list.pop(0) : list의 맨 앞의 요소 제거
# list.pop() : list의 맨 뒤의 요소 제거
#참고 사이트
# https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/Queue.py