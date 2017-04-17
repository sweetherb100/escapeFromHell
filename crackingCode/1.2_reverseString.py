# Python 메소드
# 1) for ch in str :
# str 문자열의 각 문자를 for loop을 돌면서 받는다.


#Method 1 (but too easy for the interview)
def reverseString(str):
    return str[::-1]

#Method 2 (Use Stack)
def reverseString2(str):
    stack=[]
    for ch in str:
        stack.append(ch)

    result =""
    while len(stack)>0 :
        result += stack.pop()

    return result

print(reverseString("ABCD"))
print(reverseString2("ABCD"))


