'''
Write a method to perform basic string compressions using the counts of repeated
if the compressed string would not become smaller than the original string, then return original string
input : aabcccaa
output : a2b1c4a2
(Assume duplicate characters are aligned/linked together)

*Space need : buffer, count, output

*Python
1) str(num) : num -> string
2) output+=ch : append string(append string with char)
'''

########### MY code is wrong because aabcccaa returns as a4b1c3!!!!
### should use the compressword definition
### Look at compressWords_deliveryHero.py!!!

#If order matters: use vector(its index as the ASCII code)
def compressword3(input):
    buffer=[0]*256 #number of count (256 characters of ASCII code)
    charlist = [] #visited char in order
    result=""

    for ch in input: #for loop in input: O(N)
        if buffer[ord(ch)] is 0: #access in vector: O(1)
            charlist.append(ch)
            buffer[ord(ch)]=1
        else:
            buffer[ord(ch)]+=1

    for ch in charlist: #for loop in charlist: O(N)
         result+=ch
         result+=str(buffer[ord(ch)])

    #Exception: compressed string has same length as the original string
    if len(input) <= len(result):
        return input

    return result

def compressword4(input):
    dict={} #number of count
    charlist = [] #visited char in order
    result=""

    for ch in input: #for loop in input: O(N)
        if ch not in dict: #access in hashmap: O(1)
            charlist.append(ch)
            dict[ch]=1
        else:
            dict[ch]+=1

    for ch in charlist: #for loop in charlist: O(N)
         result+=ch
         result+=str(dict[ch])

    #Exception: compressed string has same length as the original string
    if len(input) <= len(result):
        return input

    return result

print("Using for loop; space: 2 vectors")
print(compressword3("abbcccccccd"))
print(compressword3("abc"))
print(compressword3("aabcc")) #aabcc is shorter than a2b1c2. so return aabcc

print("Using for loop; space: vector/hashmap")
print(compressword4("abbcccccccd"))
print(compressword4("abc"))
print(compressword4("aabcc")) #aabcc is shorter than a2b1c2. so return aabcc

# Not intuitive...
# def compressword(input):
#     buffer =None
#     output=""
#     cnt=1
#     for ch in input:
#         if buffer is None: #First moment
#             output+=ch #append
#             buffer= ch
#         else:
#             if buffer==ch:
#                 cnt+=1
#             else:
#                 output+=str(cnt) #append
#                 cnt =1
#                 output+=ch #repeat first if clause
#                 buffer=ch
#     output+=str(cnt) #last append
#
#     if len(output) > len(input):
#         return input
#     else :
#         return output
# print("Using for loop; space: char, int")
# print(compressword("abbcccccccd"))
# print(compressword("abc"))
# print(compressword("aabcc")) #aabcc is shorter than a2b1c2. so return aabcc


#If order doesn't matter: use HashMap (but order should matter)
# def compressword2(input):
#     dict={}
#     result=""
#     for ch in input: #for loop in input: O(N)
#         if ch not in dict.keys():
#             dict[ch]=1
#         else:
#             dict[ch]+=1
#
#
#      #but may not be in order!!!
#     for key,value in dict.items(): #for loop in dict: O(N)
#         result+=key
#         result+=str(value)
#
#     #Exception: compressed string has same length as the original string
#     if len(input) <= len(result):
#         return input
#
#     return result
# print("Using for hashMap")
# print(compressword2("abbcccccccd"))
# print(compressword2("abc"))
# print(compressword2("aabcc")) #aabcc is shorter than a2b1c2. so return aabcc