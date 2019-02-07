'''
* Python
for ch in str :
get each char in String str

#Method 1 (but too easy for the interview)
def reverseString(str):
    return str[::-1]
'''

#Method 2: Use Stack
def reverseString(str):
    result = ""
    stack=[]
    for ch in str: #for loop in str: O(n)
        stack.append(ch)

    while len(stack) > 0 : #pop from stack: O(n)
        result += stack.pop()

    return result

print(reverseString("ABCD"))


