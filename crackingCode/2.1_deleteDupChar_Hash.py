# case1: in order; use Set
def deleteDuplicate(str):
    result=""
    strset=set() #initialize in hashSet

    for ch in str: #for loop in str: O(N)
        if ch in strset: #if exist ch
            continue
        else:
            strset.add(ch)
            result += ch  #string form

    return result

print(deleteDuplicate("3456474666"))

# # case1: no need for order; use Set
# def deleteDuplicate2(str):
#     result = ""
#     strset=set(str) #add in hashSet: O(1); but there are N element: O(N)
#     print(strset) #{'6', '3', '5', '7', '4'}
#
#     for ch in strset: #for loop in strset:O(N)
#         result+=ch
#
#     return result
# print(deleteDuplicate2("3456474666"))