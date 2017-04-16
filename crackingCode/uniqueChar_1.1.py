# To Think About
# 1) Compare each characters? : O(N^2). very simple
# 2) Any better solutions? : HashTable?
# 3) What if we use hash? O(N)
# 4) Ok... can we imporve more?
# 5) If charcters are asci characters(total 256 characters),
# >56 must be duplicate
#
# Python 메소드
# 1) ord("X") : 실제 문자 -> ASCII 코드 번호
# 2) chr(90) : ASCII 코드 번호 -> 실제 문자

def isUniqChars(str):
    #assume characters are ASCII, total 256 characters
    #if the string is greater than 256, there is duplicate
    if len(str) > 256:
        return False
    hash = [False]*256

    for ch in str:
        if hash[ord(ch)] is True:
            return False
        else:
            hash[ord(ch)] = True
    return True

print(isUniqChars("ABCDE"))
print(isUniqChars("ABCDEAA"))