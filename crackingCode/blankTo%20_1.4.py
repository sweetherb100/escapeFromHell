# 과정
# 1) str.strip() : 문자열 양쪽 공백을 모두 지움
# 2) str.replace("","%20") : replace

def replace(str):
    return str.strip().replace(" ","%20")

print(replace("    Mr    John Smith"))