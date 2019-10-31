'''
Replace
1) str.strip(): strip front and the end away
2) str.replace("","%20") : replace
'''

def replace(str):
    return str.strip().replace(" ","%20")

print(replace("    Mr    John Smith")) #Mr%20%20%20%20John%20Smith
# return str.replace(" ","%20") : %20%20%20%20Mr%20%20%20%20John%20Smith