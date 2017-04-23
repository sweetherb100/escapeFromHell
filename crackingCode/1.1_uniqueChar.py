'''
* To Think About
1) Compare each characters? : O(N^2). very simple
2) Any better solutions? : HashTable?
3) What if we use hash? O(N)
4) Ok... can we improve more?
5) If characters are ascii characters(total 256 characters),
>56 must be duplicate

* Python
1) ord("X") : char -> ASCII code number
2) chr(90) : ASCII code number -> char
'''

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