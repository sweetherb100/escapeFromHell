'''
Replace
1) str.strip()
2) str.replace("","%20") : replace
'''

def replace(str):
    return str.strip().replace(" ","%20")

print(replace("    Mr    John Smith"))