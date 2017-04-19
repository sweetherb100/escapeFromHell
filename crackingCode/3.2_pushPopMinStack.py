'''
*Question : How would you design a stack which, in addition to push and pop,
also has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.

*Python
#1)peek() method : use array[-1] (the last element)

*My own way
'''

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
