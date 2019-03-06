# print("AAAA\t sgjdkgdlj \nd asdjgkgl")
'''
Pretty print a json object using proper indentation.

Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Example 1:

Input : {A:"B",C:{D:"E",F:{G:"H",I:"J"}}}
Output : 
{ 
    A:"B",
    C: 
    { 
        D:"E",
        F: 
        { 
            G:"H",
            I:"J"
        } 
    } 
}
Example 2:

Input : ["foo", {"bar":["baz",null,1.0,2]}]
Output : 
[
    "foo", 
    {
        "bar":
        [
            "baz", 
            null, 
            1.0, 
            2
        ]
    }
]
[] and {} are only acceptable braces in this case.

Assume for this problem that space characters can be done away with.
Your solution should return a list of strings, where each entry corresponds to a single line. The strings should not have “\n” character in them.
'''


### solution shouldnt have \n but just list of strings and each element represents the line
class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        result = []
        temp=""
        indentcnt = 0

        ### DONT FORGET TO APPEND INDENTCNT FOR EVERY RESULT APPEND
        for i in range(len(A)):
            if A[i] in ('[', '{'):
                if temp != "" :  #not emptyd
                    result.append('\t'*indentcnt +temp)
                    temp="" #reset

                result.append('\t'*indentcnt + A[i])
                indentcnt += 1

            elif A[i] in (']', '}'):
                if temp != "":  # not empty
                    result.append('\t'*indentcnt +temp)
                    temp = ""  # reset

                indentcnt -= 1
                result.append('\t'*indentcnt + A[i])

            elif A[i] == ',': #after comma, character or { can come next. For now, I assumed that the character would come put didn't consider {
                if temp != "": #not empty
                    result.append('\t'*indentcnt+ temp +A[i])
                    temp="" #reset
                else: #CASE }, (BUT THIS WAS NOT MENTIONED AS THE EXAMPLE...)
                    result[-1] = result[-1]+A[i] #change directly maybe because it is reference?!


            else:  # just character
                temp+=A[i]

        return result


solution = Solution()
# print(solution.prettyJSON("{\"id\":100,\"firstName\":\"Jack\",\"lastName\":\"Jones\",\"age\":12}"))
ls = solution.prettyJSON("[\"foo\", {\"bar\":[\"baz\",null,1.0,2]}]")
for i in range(len(ls)):
    print(ls[i])
# print(solution.prettyJSON2("{\"id\":100,\"firstName\":\"Jack\",\"lastName\":\"Jones\",\"age\":12}"))
# string1 = "aaaa" + "\n"*2 + "\t" * 3 + "ccc"
# print(string1)

'''
    def prettyJSON2(self, st):
        # ans is list of string to print
        ans = []
        line = ''
        # no of tab required
        tab = 0
        for s in st:
            # to avoid empty lines
            line = line.strip()
            if s in ['{', '[', '}', ']', ]:
                if line:
                    ans.append('\t' * tab + line)
                # append is after decreasing tab count
                if s in ['}', ']']:
                    tab -= 1
                ans.append('\t' * tab + s)
                if s in ['{', '[']:
                    tab += 1
                line = ''
                continue

            if s in [',']:
                line += s
                # if only comma, then it should be in previous line
                if line == ',':
                    ans[-1] += s
                elif line:
                    ans.append('\t' * tab + line)
                line = ''
            else:
                line += s

        return ans
'''