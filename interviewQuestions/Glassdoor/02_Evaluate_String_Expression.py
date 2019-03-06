### Given a string of arithmetic expression, composed of numbrs,'+',and '*',
# calculate the result (e.g. 2+4*5*7)

### Data structure : 2 STACKS

### For simplicity, for now work with one digit number
### For simplicity, the string expression is valid


class Solution():
    def evaluate_expression(self, str):
        numstack=[]
        operstack =[]
        cur=0

        while cur < len(str) :
            if str[cur] not in ("+", "*"): #if it is number
                numstack.append(int(str[cur])) ### BE CAREFUL WITH CONVERSION
                cur+=1 #update

            elif str[cur] == "+":
                operstack.append(str[cur]) #save + for now and do the calcuation later
                cur+=1

            elif str[cur] == "*": #4*5
                val1 = numstack.pop()
                val2= int(str[cur+1]) #guaranteed to be exist because it will be after * #BE CAREFUL WITH CONVERSION
                val= val1*val2
                numstack.append(val)
                cur+=2

        while len(operstack) != 0: #there will be only plus, 2+4+35
            val1=numstack.pop()
            operstack.pop()
            val2=numstack.pop()
            numstack.append(val1+val2)

        return numstack.pop()

sol =Solution()
print(sol.evaluate_expression("2+4+5*7"))
# sol.evaluate_expression("4+13//5")
# "4+13/5"


