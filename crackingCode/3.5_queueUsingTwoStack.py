#implement queue using two stacks

class Stack:
    def __init__(self):
        self.items=[]
        self.max_size=3

    def push(self,item):
        self.items.append(item)

    def pop(self):
        #여기서는 단순히 pop만하는게 아니라 값도 return 시켜야
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def printStack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class myQueue:
    def __init__(self):
        self.st1=Stack()
        self.st2=Stack()

    def enqueue(self,item):
        self.st1.push(item)

    def dequeue(self):
        if self.st2.is_empty():
            while self.st1.is_empty() is False:
                self.st2.push(self.st1.pop())

        return self.st2.pop()


myq=myQueue()
myq.enqueue(1)
myq.enqueue(2)
myq.enqueue(3)
print(myq.st1.printStack())
print(myq.dequeue())
print(myq.dequeue())
print(myq.dequeue())

