'''
* To Think About
1) Compare each characters? : O(N^2). very simple
2) Any better solutions? : HashTable (HashSet)? Vector? 
3) Ok... can we improve more?
=> If characters are ascii characters(total 256 characters), if more than 256, there must be duplicate

* Python
1) ord("X") : char -> ASCII code number
'''

#assume characters are ASCII, total 256 characters
def isUniqChars(str):
    #exception: if the string is greater than 256, there is duplicate
    if len(str) > 256:
        return False
    hash = [False]*256

    for ch in str: # for loop in str: O(N)
        if hash[ord(ch)] is True: #access in vector: O(1); ord(ch) acts like an index
            return False
        else:
            hash[ord(ch)] = True #access/add in vector: O(1) (already initialized with full size vector)
    return True

def isUniqChars2(str):
    #exception: if the string is greater than 256, there is duplicate
    if len(str) > 256:
        return False

    hashset=set(str) #add in hashSet: O(1) but there is N number of element; O(N)

    if len(hashset) != len(str):
        return False

    return True

print("Vector as data structure")
print(isUniqChars("ABCDE"))
print(isUniqChars("ABCDEAA"))

print("HashSet as data structure")
print(isUniqChars2("ABCDE"))
print(isUniqChars2("ABCDEAA"))