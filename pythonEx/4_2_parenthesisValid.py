#TIP : python 자체적으로 list가 stack 형태로 되어있음
#stack-> list, append, pop 활용!!

def cal_validation(input):
    parenList={'{':'}',
               '[':']',
               '(':')'}

    stack=[];
    inputList = list(input)
    try :
        for data in inputList:
            if data in parenList.keys():
                stack.append(data)
            if data in parenList.values():
                if parenList[stack.pop()] != data:
                    return False #'Wrong. Parenthesis not matching'
                    break


    except:
        return False #IndexError: pop from empty list (sth wrong at the end)

    if len(stack) != 0: #(sth wrong at the front)
        return False

    return True


print(cal_validation("[[()[]{}]]"))


# algo_test (간단한데 python 문법 헷갈려서 헤맨 부분...)
# list=[1,2,3,4,5,6]
# print(list.pop())
#
# wintable = {
#     '가위':'보',
#     '바위':'가위',
#     '보':'바위'
# }
# print(wintable['가위'])
#
# parenList = {
#              '{': '}',
#              '[': ']',
#              '(': ')'}
# print(parenList['('])