#stack : 1)push(stack-overflow 고려)
        #2)pop(stack-underflow 고려) 메소드 구현

#문제 : 하나의 배열에 3개의 stack 만들기.
# 따라서 self.array=[None]*stack_size*3으로 선언

#python 메소드
# 1) self.array=[None]*stack_size*3
# 각 인자에 None 추가하고 크기까지 한꺼번에 설정 가능
# 2) class 이름 선언 시에 class에 괄호가 있든 없든 상관 없음 (stacks_in_array()도 OK)


class stacks_in_array: #class에 괄호가 있든 없든 상관 없음 (stacks_in_array()도 OK)
    def __init__(self,stack_size):
        self.array=[None]*stack_size*3
        #각 인자에 None 추가하고 크기까지 한꺼번에 설정 가능
        self.stack_size = stack_size

        self.stack1_bottom=0
        self.stack1_top=self.stack1_bottom+self.stack_size
        self.stack2_bottom=self.stack1_top
        self.stack2_top=self.stack2_bottom+self.stack_size
        self.stack3_bottom=self.stack2_top
        self.stack3_top=self.stack3_bottom+self.stack_size

        self.stack1_idx=0
        self.stack2_idx=self.stack1_idx+self.stack_size
        self.stack3_idx=self.stack2_idx + self.stack_size

    def push_stack1(self,val):
        if self.stack1_idx==self.stack1_top: #stack overflow
            print("stack1 is full")
            return False
        else:
            self.array[self.stack1_idx]=val
            self.stack1_idx=self.stack1_idx +1
            return True

    def push_stack2(self,val):
        if self.stack2_idx==self.stack2_top: #stack overflow
            print("stack2 is full")
            return False
        else:
            self.array[self.stack2_idx]=val
            self.stack2_idx=self.stack2_idx +1
            return True

    def push_stack3(self,val):
        if self.stack3_idx==self.stack3_top: #stack overflow
            print("stack3 is full")
            return False
        else:
            self.array[self.stack3_idx]=val
            self.stack3_idx=self.stack3_idx +1
            return True

    def pop_stack1(self):
        if self.stack1_idx==self.stack1_bottom: #stack underflow
            print("stack1 is empty")
            return False
        elif self.stack1_bottom < self.stack1_idx:
            # index has been increased at push method. Therefore decrease when pop
            self.stack1_idx = self.stack1_idx -1
            self.array[self.stack1_idx] = None
            return True
        else: #just in case
            return False

    def pop_stack2(self):
        if self.stack2_idx==self.stack2_bottom: #stack underflow
            print("stack2 is empty")
            return False
        elif self.stack2_bottom < self.stack2_idx:
            # index has been increased at push method. Therefore decrease when pop
            self.stack2_idx = self.stack2_idx -1
            self.array[self.stack2_idx] = None
            return True
        else: #just in case
            return False

    def pop_stack3(self):
        if self.stack3_idx==self.stack3_bottom: #stack underflow
            print("stack1 is empty")
            return False
        elif self.stack3_bottom < self.stack3_idx:
            # index has been increased at push method. Therefore decrease when pop
            self.stack3_idx = self.stack3_idx -1
            self.array[self.stack3_idx] = None
            return True
        else: #just in case
            return False

    def printArray(self):
        return self.array

arrayStack=stacks_in_array(3)
print(type(arrayStack)) #<class '__main__.stacks_in_array'>
print(arrayStack) #<__main__.stacks_in_array object at 0x02A9A470>
print(arrayStack.printArray()) #[None, None, None, None, None, None, None, None, None]
arrayTest = [None]*3*3
print(arrayTest) #[None, None, None, None, None, None, None, None, None]
print(type(arrayTest)) #<class 'list'>
print('**************above console is test')
arrayStack.push_stack1(1)
arrayStack.push_stack1(2)
arrayStack.push_stack1(3)
# arrayStack.push_stack1(4)
print(arrayStack.printArray()) #[1, 2, 3, None, None, None, None, None, None]
arrayStack.pop_stack1()
print(arrayStack.printArray()) #[1, 2, None, None, None, None, None, None, None]
arrayStack.pop_stack1()
print(arrayStack.printArray()) #[1, None, None, None, None, None, None, None, None]
arrayStack.pop_stack1()
print(arrayStack.printArray()) #[None, None, None, None, None, None, None, None, None]
arrayStack.pop_stack1() #stack1 is empty