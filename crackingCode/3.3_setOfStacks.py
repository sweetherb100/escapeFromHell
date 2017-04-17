# Question : Set of Stacks
# stack 문제 : push(over flow), pop(under flow) 고려
# (그 외 peek(), is_empty(), size())

class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def printStack(self):
        return self.items

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)


class Stacks():
    def __init__(self):
        self.stacklist=[]
        self.max_stack_size=3
        #initialize first stack in the stack list
        self.stacklist.append(Stack())

    def push(self,item):
        st=self.getLastStack()
        if self.max_stack_size == st.size(): #overflow
            newSt = Stack()
            newSt.push(item)
            self.stacklist.append(newSt)
        else:
            st.push(item)

    def pop(self):
        st=self.getLastStack()
        if st.is_empty() is False:
            st.pop()
            if st.is_empty(): #to match the count of Stacks
                self.stacklist.pop()
        else :
            print('there is no item in Stacks')

        ###########질문올리기
        # if st.is_empty(): #underflow
        #     print('len(self.stacklist) ',len(self.stacklist))
        #     self.stacklist.pop()
        #     print('len(self.stacklist) ', len(self.stacklist))
        #     st = self.getLastStack()
        #     st.pop()
        # else:
        #     st.pop()

    def getLastStack(self):
        return self.stacklist[-1]

    def getStackCount(self):
        return len(self.stacklist)

    def printStacks(self):
        result=[]
        for stack in self.stacklist:
            for item in stack.items:
                result.append(item)
        return result


#Stack()클래스 자체를 쓰는게 아니라 Stacks()클래스로 구현
stacks=Stacks()
stacks.push(5)
stacks.push(3)
stacks.push(2)
stacks.push(7)
print(stacks.printStacks()) #[5, 3, 2, 7]
print(stacks.getStackCount()) #2
stacks.pop()
print(stacks.printStacks()) #[5, 3, 2]
print(stacks.getStackCount()) #1
stacks.pop()
print(stacks.printStacks()) #[5, 3]
print(stacks.getStackCount()) #1







