# [Question]
# Write a method to perform basic string compressions using the counts of repeated
# if the compressed string would not become smaller than the original string, then return original string
#
# input : aabcccaa
# output : a2b1c4a2

# 필요한 공간 : buffer, count, output (전제 : string의 같은 character는 이어져 있다.`)

#python 메소드
# 1) str(num) : num를 string으로 변환

def compressword(input):
    buffer =None
    output=""
    cnt=1
    for ch in input:
        if buffer is None: #처음 순간
            output+=ch
            buffer= ch
        else:
            if buffer==ch:
                cnt+=1
            else:
                output+=str(cnt)
                cnt =1
                output+=ch #처음 순간 if절 다시 반복
                buffer=ch
    output+=str(cnt)

    if len(output) > len(input):
        return input
    else :
        return output

print(compressword("abbcccccccd"))
print(compressword("abc"))
print(compressword("aabcc")) #a2b1c2보다 길이 작기 때문에 aabcc로 return


