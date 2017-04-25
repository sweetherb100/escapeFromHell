'''
*Question
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

def compressword(input):
    buffer =None
    output=""
    cnt=1
    for ch in input:
        if buffer is None: #First moment
            output+=ch #append
            buffer= ch
        else:
            if buffer==ch:
                cnt+=1
            else:
                output+=str(cnt) #append
                cnt =1
                output+=ch #repeat first if clause
                buffer=ch
    output+=str(cnt) #last append

    if len(output) > len(input):
        return input
    else :
        return output

print(compressword("abbcccccccd"))
print(compressword("abc"))
print(compressword("aabcc")) #aabcc is shorter than a2b1c2. so return aabcc


