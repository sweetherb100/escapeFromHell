'''
*Question : How would you design a stack which, in addition to push and pop,
also has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
#### Technically, Push can be O(N) if I am trying to push that is bigger than its size?!?!?


*Python
1) peek() method : use array[-1] (the last element)
### CAREFUL!
2) SHOULD KEEP MINS LIST (NOT VAR) BECAUSE I CAN KEEP CALLING MINIMUM ELEMENT AFTER POP/PUSH!!!!
2) getMin DOESN'T MIN POP!! JUST CHECKING MIN (so after getMin, if I do again, it will be still same MINIMUM!!)
'''

class MinStack:
    def __init__(self):
        self.data = []          # Store all the data
        self.minData  = []      # Store the minimum element so far

    def push(self, x):
        self.data.append(x)
        # Check if we need to update the minimum value
        if len(self.minData) == 0 or x <= self.minData[-1]:
            self.minData.append(x)

    def pop(self):
        if len(self.data) == 0:
            return None
        else:
            if self.data[-1] == self.minData[-1]:
                self.minData.pop()
            return self.data.pop()

    def top(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1]

    def getMin(self):
        if len(self.minData) == 0:
            return None
        else:
            return self.minData[-1]

    def printArray(self):
        return self.data

    def printMinArray(self):
        return self.minData


st=MinStack()
st.push(5)
print(st.printMinArray())
print(st.printArray())
print("**********")

st.push(3)
print(st.printMinArray())
print(st.printArray())
print("**********")

st.push(4)
print(st.printMinArray())
print(st.printArray())
print("**********")

st.push(6)
print(st.printMinArray())
print(st.printArray())
print("**********")

st.push(1)
print(st.printMinArray())
print(st.printArray())

print("**********")

st.pop()
print(st.printMinArray())
print(st.printArray())
print("**********")

st.pop()
print(st.printMinArray())
print(st.printArray())
