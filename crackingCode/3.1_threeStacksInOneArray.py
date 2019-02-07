'''
*Question : Use single array for three stacks

top: should point to the most recent element

*class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
'''

class stacks_in_array:
    def __init__(self, stack_size):
        self.array = [None]*stack_size*3
        self.stack_size = stack_size

        self.stack1_top = -1 + 0*self.stack_size #-1 : empty
        self.stack2_top = -1 + 1*self.stack_size
        self.stack3_top = -1 + 2*self.stack_size

    def isEmpty1(self):
        return self.stack1_top == -1 + 0*self.stack_size

    def isEmpty2(self):
        return self.stack2_top == -1 + 1*self.stack_size

    def isEmpty3(self):
        return self.stack3_top == -1 + 2*self.stack_size

    def push_stack1(self,val):
        if self.stack1_top == 1*self.stack_size-1:
            print("stack1 is full")
            return False
        else:
            self.stack1_top = self.stack1_top + 1
            self.array[self.stack1_top]=val
            return True

    def push_stack2(self,val):
        if self.stack2_top == 2*self.stack_size-1:
            print("stack2 is full")
            return False
        else:
            self.stack2_top = self.stack2_top + 1
            self.array[self.stack2_top] = val
            return True

    def push_stack3(self,val):
        if self.stack3_top == 3*self.stack_size-1:
            print("stack3 is full")
            return False
        else:
            self.stack3_top = self.stack3_top + 1
            self.array[self.stack3_top] = val
            return True

    def pop_stack1(self):
        if self.stack1_top == -1 + 0*self.stack_size:
            print("stack1 is empty")
            return None
        else:
            result=self.array[self.stack1_top]
            self.array[self.stack1_top] = None
            self.stack1_top = self.stack1_top -1
            return result

    def pop_stack2(self):
        if self.stack2_top == -1 + 1*self.stack_size:
            print("stack2 is empty")
            return False
        else:
            result = self.array[self.stack2_top]
            self.array[self.stack2_top] = None
            self.stack2_top = self.stack2_top - 1
            return result

    def pop_stack3(self):
        if self.stack3_top == -1 + 2*self.stack_size:
            print("stack1 is empty")
            return False
        else:
            result = self.array[self.stack3_top]
            self.array[self.stack3_top] = None
            self.stack3_top = self.stack3_top - 1
            return result

    def peek_stack1(self):
        if self.stack1_top == -1 + 0 * self.stack_size:
            print("stack1 is empty")
            return None
        else:
            return self.array[self.stack1_top]

    def peek_stack2(self):
        if self.stack2_top == -1 + 1*self.stack_size:
            print("stack2 is empty")
            return False
        else:
            return self.array[self.stack2_top]

    def peek_stack3(self):
        if self.stack3_top == -1 + 2*self.stack_size:
            print("stack1 is empty")
            return False
        else:
            return self.array[self.stack3_top]

    def size_stack1(self):
        return (1+self.stack1_top) - 0*self.stack_size

    def size_stack2(self):
        return (1 + self.stack2_top) - 1*self.stack_size

    def size_stack3(self):
        return (1 + self.stack3_top) - 2*self.stack_size

    def printArray(self):
        return self.array

arrayStack=stacks_in_array(3) #stack size : 3

arrayStack.push_stack1(1)
arrayStack.push_stack1(2)
arrayStack.push_stack2(6)
arrayStack.push_stack2(7)
arrayStack.push_stack3(35)
print(arrayStack.printArray())
print("***size***")
print(arrayStack.size_stack1())
print(arrayStack.size_stack2())
print(arrayStack.size_stack3())
print("***peek***")
print(arrayStack.peek_stack1())
print(arrayStack.peek_stack2())
print(arrayStack.peek_stack3())

arrayStack.pop_stack1()
print(arrayStack.printArray())
arrayStack.pop_stack2()
print(arrayStack.printArray())
arrayStack.pop_stack3()
print(arrayStack.printArray())
print("***isEmpty***")
print(arrayStack.isEmpty1())
print(arrayStack.isEmpty2())
print(arrayStack.isEmpty3())
print("***size***")
print(arrayStack.size_stack1())
print(arrayStack.size_stack2())
print(arrayStack.size_stack3())

'''
    def __init__(self, stack_size):
        self.array = [None]*stack_size*3
        self.stack_size = stack_size

        self.stack1_bottom=0
        self.stack1_top=self.stack1_bottom + self.stack_size

        self.stack2_bottom=self.stack1_top
        self.stack2_top=self.stack2_bottom + self.stack_size

        self.stack3_bottom=self.stack2_top
        self.stack3_top=self.stack3_bottom + self.stack_size

        self.stack1_idx=0
        self.stack2_idx=self.stack1_idx + self.stack_size
        self.stack3_idx=self.stack2_idx + self.stack_size

    def push_stack1(self,val):
        if self.stack1_idx == self.stack1_top:
            print("stack1 is full")
            return False
        else:
            self.array[self.stack1_idx]=val
            self.stack1_idx=self.stack1_idx +1
            return True

    def push_stack2(self,val):
        if self.stack2_idx == self.stack2_top:
            print("stack2 is full")
            return False
        else:
            self.array[self.stack2_idx]=val
            self.stack2_idx=self.stack2_idx +1
            return True

    def push_stack3(self,val):
        if self.stack3_idx == self.stack3_top:
            print("stack3 is full")
            return False
        else:
            self.array[self.stack3_idx]=val
            self.stack3_idx=self.stack3_idx +1
            return True

    def pop_stack1(self):
        if self.stack1_idx == self.stack1_bottom:
            print("stack1 is empty")
            return False
        elif self.stack1_bottom < self.stack1_idx:
            #self.stack1_idx = self.stack1_idx -1
            self.array[self.stack1_idx] = None
            return True
        else: #just in case
            return False

    def pop_stack2(self):
        if self.stack2_idx == self.stack2_bottom:
            print("stack2 is empty")
            return False
        elif self.stack2_bottom < self.stack2_idx:
            self.stack2_idx = self.stack2_idx -1
            self.array[self.stack2_idx] = None
            return True
        else: #just in case
            return False

    def pop_stack3(self):
        if self.stack3_idx == self.stack3_bottom:
            print("stack1 is empty")
            return False
        elif self.stack3_bottom < self.stack3_idx:
            self.stack3_idx = self.stack3_idx -1
            self.array[self.stack3_idx] = None
            return True
        else: #just in case
            return False

    def printArray(self):
        return self.array
'''