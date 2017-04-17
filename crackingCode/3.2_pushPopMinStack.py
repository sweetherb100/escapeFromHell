#stack has min function O(1)
#my way

#python 메소드
#1)peek() 구현 : array[-1] (맨 마지막 element)

class stack():
    def __init__(self):
        self.items = []
        self.mins=[]

    def push(self,item):
        self.items.append(item)
        if len(self.mins) ==0 : #first push
            self.mins.append(item)
        elif item < self.mins[-1]:
            self.mins.append(item)
        elif self.mins[-1] < item:
            self.mins.append(self.mins[-1])

    def pop(self):
        self.items.pop()
        self.mins.pop()

    def getminimum(self):
        return self.mins[-1]

    def printArray(self):
        return self.items

    def printMinArray(self):
        return self.mins

st=stack()
st.push(5)
st.push(3)
st.push(4)
st.push(1)
print(st.printMinArray())
print(st.getminimum())
st.pop()
print(st.getminimum())
