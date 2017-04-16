# 2개의 String이 anagram인지 판별 (서로 permutation인지 판별)
# 기본 아이디어 :
# Sorting해서 판별
#
# 추가 고려해야될 변수
# 1) 대소문자가 다를 경우
# 2) 공백 값이 사이에 있을 경우
# 3) 문자열 양 끝에 고백이 있는 경우
#
# python 메소드
# 1) str.lower() : 문자열을 소문자로 치환
#
# 2) str.upper() : 문자열을 대문자로 치환
#
# 3) str.strip() : 문자열 양쪽 공백을 모두 지움
#
# 4) sorted('XXXX') : String을 sorted된 list형태로 return
# ex) sorted('digkwda') -> ['a', 'd', 'd', 'g', 'i', 'k', 'w']
#
# 5) "구분자".join(list) : 리스트의 각 요소들을 하나의 합친 문자열로 반환. 요소들은 "구분자로 구분하여 표현 가능
# food = [ "123", "자장면", "짬뽕", "탕수육", "물만두", "팔보채" ]
# 5-1) 요소들 사이에 공백 넣기 (구분자는 공백)
# print " ".join(food)
# 123 자장면 짬뽕 탕수육 물만두 팔보채
#
# 5-2) 모든 요소들을 하나로 연결하여 출력 (구분자 없음)
# print "".join(food)
# 123자장면짬뽕탕수육물만두팔보채
#
# 5-3) 슬래쉬(/)기호를 구분자로 넣은 후 연결하여 출력
# print "/".join(food)
# 123/자장면/짬뽕/탕수육/물만두/팔보채
#
# 5-4) 줄바꿈 문자를 구분자로 하여 출력
# print "\n".join(food)
# 123
# 자장면
# 짬뽕
# 탕수육
# 물만두
# 팔보채

def anagram(str1, str2) :
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        return True
    else:
        return False

print(anagram("listen","silent"))
print(anagram("lisTeN","SilEnt"))
print(anagram("l i s T e N"," Si lEnt "))