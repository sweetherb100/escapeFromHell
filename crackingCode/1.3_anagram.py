'''
*Anagram (=whether it is permutation to each other)
Sort 2 String and Compare

*Extra Consideration
1) upper/lower case
2) space inbetween
3) space in each end side of string

* Python
1) str.lower() : string to lower case. no return
2) str.upper() : string to upper case. no return
3) str.strip() : remove space at each end side of string. no return
4) sorted('XXXX') : return sorted list
5) list.sort(): sort list. no return
6) "seperator".join(list) : combine list into string. 
chars = [ "A", "B", "C", "D", "E", "F" ]
6-1) put space in between
print " ".join(chars) : A B C D E F
6-2) no seperator.
print "".join(chars) : ABCDEF
6-3) 슬래쉬(/) as seperator
print "/".join(chars) : A/B/C/D/E/F
6-4) enter (\n)
print "\n".join(chars) :
A
B
C
D
E
F
'''

def anagram(str1, str2) :
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        return True
    else:
        return False

print(anagram("listen","silent"))
print(anagram("lisTeN","SilEnt"))
print(anagram("l i s T e N"," Si lEnt "))

