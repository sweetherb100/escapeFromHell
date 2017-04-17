class Stack:
    def __init__(self):
        self.items = []
        self.max = 3

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Stacks():
    def __init__(self):
        self.stacklist = []
        self.max_stack_size = 3
        #initialize first stack in stack list
        self.stacklist.append(Stack())

    def push(self, item):
        st = self.getLastStack();
        if self.max_stack_size == st.size():
            new_st = Stack()
            new_st.push(item)
            self.stacklist.append(new_st)
        else:
            st.push(item)

    def pop(self):
        st = self.getLastStack();
        if st.is_empty():
            self.stacklist.pop()
            st = self.getLastStack();
            st.pop()
        else:
            st.pop()

    def getLastStack(self):
        return self.stacklist[len(self.stacklist)-1]

    def getStacksCount(self):
        return len(self.stacklist)

    def printStacks(self):
        result = []
        for st in self.stacklist:
            for item in st.items:
                result.append(item)
        return result

stacks=Stacks()
stacks.push(5)
stacks.push(3)
stacks.push(2)
stacks.push(7)
print(stacks.printStacks())
print(stacks.getStacksCount())
stacks.pop()
print(stacks.printStacks()) #왜 2가 나오지????
print(stacks.getStacksCount())
stacks.pop()
print(stacks.printStacks()) #왜 2가 나오지????