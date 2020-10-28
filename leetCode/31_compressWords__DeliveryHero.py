def compressWords(S):
        #Exception: empty string
        if len(S) == 0:
            return ""

        buffer=None
        output=""
        cnt=1

        for ch in S:
            #Exception: it is not a character
            if (97 > ord(ch.lower()) or ord(ch.lower()) > 122):
                return "error"

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

        return output


print(compressWords("aaaabbaaa")) #a4b2a3
print(compressWords("aaaabb")) #a4b2
print(compressWords("256")) #error

