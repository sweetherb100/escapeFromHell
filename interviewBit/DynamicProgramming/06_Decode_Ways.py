'''
Dynamic Programming:
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a "non-empty" string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input "1226":
Output : 5 (12 26, 12 2 6, 1 2 26, 1 2 2 6 => abbf, abz, avf...)
'''

## BETTER TO HAVE EXTRA MEMORY TO KEEP FOR THE ALREADY CALCULATED ONES
class Solution():
    def __init__(self):
        self.mem=[] #vector is enough for the memory because index itself is the key
        ### DONT GET CONFUSED THAT ALL e.g. k=3 IS THE SAME REGARDLESS OF STRING => NO
        ### ONLY IN SPECIFIC STRING, e.g. k=3 WILL BE THE SAME

    def numDecodings(self, string):
        self.mem = [None] * (len(string) +1) # +1 for simplicity because k is starting from 1,2,3,4,5
        return self.decode_helper(string, len(string)) #starting full length (I will decrease as the recursion goes on)


    def decode_helper(self, string, k):
        # base condition: needed to have 2 base conditions because we are using k-1, k-2 2 recursive
        if k == 0:
            self.mem[k]=0
            return 1

        s = len(string) - k # first index that I am interested to decode
        if k == 1 and string[s] != "0": #Exception that with 1 digit, 0 cannot be decoded
            self.mem[k]=1
            return 1

        if string[s] == "0":  # when starting with 0
            return 0  # no  need to decode the rest


        #recursion
        if self.mem[k-1] is None:
            result = self.decode_helper(string, k-1) #interested in the rest of k-1
            self.mem[k-1] = result #save
        else:
            result = self.mem[k-1] #reuse

        if int(string[s:s+2]) <= 26 : #first 2 strings that I am interested to decode ### BE CAREFUL WITH CONVERSION
            if self.mem[k-2] is None:
                val = self.decode_helper(string, k-2)
                result += val
                self.mem[k-2]=val #save
            else:
                result +=self.mem[k-2] #reuse

        return result

sol= Solution()
print(sol.numDecodings("1226"))