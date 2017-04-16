# stack은 언제 사용하느냐?
# 1) Browser back button
# 2) DFS (Depth First Search)
# -------------
# | <- <- <-
# | <- <- <-
# -------------
class Stack:
    def __init__(self):
        self.items=[]
        self.max=5

    def push(self,item):
        if len(self.items) < self.max:
            self.items.append(item)
        else:
            print("abort push in order to prevent stack overflow")

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
        else:
            print("abort push in order to prevent stack underflow")

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()
#[1,2,3]
stack.pop()
stack.print_stack()
#[1,2]
print(stack.peek())
#2
print(stack.is_empty())
print(stack.size())

#참고 사이트
# https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/Stack.py