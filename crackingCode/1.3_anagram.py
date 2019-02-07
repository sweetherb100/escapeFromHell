'''
*Anagram: whether it is permutation to each other
Method1: Sort 2 strings and Compare
Method2: Use HashMap as data structure

*Extra Consideration
1) upper/lower case
2) space inbetween
3) space in each end side of string

* Python
1) str.lower() : string to lower case. no return
2) str.upper() : string to upper case. no return
3) str.strip() : remove space at each end side of string. no return
4) "seperator".join(list) : combine list into string. 
chars = [ "A", "B", "C", "D", "E", "F" ]
4-1) put space in between
print " ".join(chars) : A B C D E F
4-2) no seperator.
print "".join(chars) : ABCDEF
4-3) 슬래쉬(/) as seperator
print "/".join(chars) : A/B/C/D/E/F
4-4) enter (\n)
print "\n".join(chars)
'''

def anagram(str1, str2) :
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        return True
    else:
        return False

# Using hashmap
# Umm....but if there is 2 l and 2 s, cannot differentiate with HashMap!!
def anagram2(str1, str2) :
    dict={} #instead of True/False flag, save the number of visits

    for i in range(len(str1)):
        if str1[i] not in dict:
            dict[str1[i]]=1 #appears one time
        else:
            dict[str1[i]] += 1


    for i in range(len(str2)):
        if str2[i] not in dict: #not anagram
            return False
        else:
            dict[str2[i]] -= 1

    for key in dict.values():
        if key != 0:
            return False

    return True


print(anagram2("llisten","lsilent"))
#print(anagram2("lisTeN","SilEnt"))
#print(anagram2("l i s T e N"," Si lEnt "))


'''
    dict={} #initialize

    if len(str1) != len(str2):
        return False

    #Exception: spaces in between; lower/upper case
    for i in range(len(str1)): #for loop in str1: O(N)
        if str1[i] != " ":
            dict[str1[i].lower()]=False


    for i in range(len(str2)): #for loop in str2: O(N)
        if (str2[i] != " ") and (str2[i].lower() in dict.keys()): #Find key in hashMap: O(1)
            dict[str2[i].lower()] = True

    #print(dict.keys())
    #print(dict.items())
    #print(dict.values()) # BE CAREFUL!!! dict.items() always with key,value

    if False in dict.values(): #Find value in hashMap: O(N)
        return False

    return True
'''
