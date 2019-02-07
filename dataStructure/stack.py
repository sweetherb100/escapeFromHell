'''
*Outline
1) data type : list
2) methods : push, pop, peek, is_empty, size
3) overflow (when push), underflow(when pop) needed to be considered

*When stack is used?
1) Browser back button
2) DFS (Depth First Search)
'''

class Stack:
    def __init__(self):
        self.items=[]
        self.max=5

    def push(self,item):
        if len(self.items) < self.max:
            self.items.append(item)
        else: #overflow
            print("abort push in order to prevent stack overflow")

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
        else: #underflow
            print("stack is empty")

    def peek(self):
        return self.items[-1] #simpler than len(self.items)-1

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack() #[1,2,3]
stack.pop()
stack.print_stack() #[1,2]
print(stack.peek()) #2
print(stack.is_empty())
print(stack.size())
