def solution(S):
        #Exception: empty String
        if len(S) == 0:
            return ""

        buffer =None
        output=""
        cnt=1

        for ch in S:
            #Exception: it is not a character (after converting to ASCII, it should be in range 256)
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


# print(solution("aaaabbaaa")) #a6b2
# print(solution("aaaabb")) #a6b2
# print(solution("256")) #a6b2
print(ord(str("2").lower()))


# def isalpha(self, charac):
#     if 97 <= ord(charac.lower()) and ord(charac.lower()) <= 122:
#         return True
#     return False
print(ord('a'))
print(ord('z'))