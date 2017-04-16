'''
print('안녕','나는','천재', '야','나는 다리가', 2, '개 있어')
identity = '지구인'
number_of_leg= 4
print('안녕','나는',identity, '이야','나는 다리가', number_of_leg, '개 있어')

# 에벌레에벌레에벌레에벌레에벌레에벌레에벌레에벌레

my_name = 'Jiyoung Kim'
my_age=10
print(my_name, ' is', my_age)
my_age = my_age+1
print(my_name, ' is', my_age)
power = 2**10
print(my_name, ' is', power)

people = 3
apple = 20
if people < apple / 5:
	print('hasgjdgksda')
	
if apple % people > 0:
	print ('agjkdagldjgk')

if False:
	print('블럭에 속한 코드')
	print('메롱')
	
	if False:
		print('이프 안에 이프 펄스')
	
	if True:
		print('이프 안에 이프 트루')
		
	print('블럭의 끝 코드')
	
print('실행 끝')

SCISSOR = '가위'
ROCK ='바위'
PAPER = '보'

WIN = '이겼다'
DRAW='비겼다'
LOSE ='졌다'

mine = '가위'
yours='바위'

if mine==yours:
	result=DRAW
else:
	result='이기거나 지거나'
	
print(result)

def print_sqrt(a,b,c):
	r1=(-b+(b**2 -4*a*c)**0.5) / (2*a)
	r2=(-b-(b**2 -4*a*c)**0.5) / (2*a)

	print('해는 {} 또는 {}' .format(r1,r2))

x=1
y=2
z=-8
print_sqrt(z,y,z) #함수 호출


def function():
	print('안녕')
	
function() #함수 호출


def print_round(number):
	rounded=round(number)
	print(rounded)
	
print_round(3.5)


def add_10(value):
	result = value+10
	return result
	
add_10(42)


#원하는 모양으로 쉽게 변환하는 명령어 : format
number = 20
greeting='Hello'
place = 'Korea'
welcome ='welcome'

#new way
base = '{}번 손님, {}.{}에 오신 것을 {}!'
new_way = base.format(number, greeting, place, welcome)
print(new_way)


string1= 'Some text'
string2= "어떤 텍스트"
string3='{}도 {}도 지금 이것도 문자열'.format(string1,string2)

print(string1,string2,string3)

quote= '문법검사기 왈 "직접인용은 큰따옴표다!"'
emphasize = "'문법검사기'를 인용하다니"
#error = "엄마친구아들이 파이써닝 좋아"라고 했대"

#long_string=(따옴표 3개) 첫째줄은 좋은데
#둘째줄도 괜찮을까 (따옴표 3개)
#이렇게 줄 바꿈 string은 (따옴표 3개)로 이용
quote2= """가끔은 '와 "를 모두 쓰기도 해"""
print(quote2)


#python은 내가 쓴 숫자 그대로 출력해주지는 않는다
five1=5
five2=5.0
five3=5.0000 #결과 5.0

print(five1)
print(five2)
print(five3)

print(6/5) #결과 1.2
div1= 6/5
div2=9//5 #몫 개념
div3=9%5 #나머지 개념
print(div2) #결과 1(몫 또는 버림의 개념) (숫자 1만 나오게끔 하려면 //)
print(div3)

print(int(5.0))
print(float(5))
print(5*1.0)


mine=input()
print('mine:',mine)

mine=input('가위 바위 보 중 하나를 내주세요 > ')
print('mine : ',mine)

print('hello my nmae is jiyoung kim ', end='just kidding')


#리스트
list1=['가위','바위','보']
list2= [1,2,3,3,5,6,7,77]

print(list1)
print(list2)
print(list1[1])
print(list1[-1]) #뒤에서 첫번째
print(list1[-3]) #뒤에서 세번째


#리스트 수정
list2=[33,53,552,6564,753,523]
print(list2)

list2.append(16)
print(list2)

list3= list2+[252,352]
print(list3)

n = 12
ownership = n in list3
print(ownership)

n=753
if n in list3:
	print('{}은 있어!'.format(n))
	
del list2[2] #index
print(list2)
list2.remove(53) #값
print(list2)


#for in list
patterns = ['가위','보','보','가위','가위','가위','보','가위','가위','보']
for pattern in patterns:
	print(pattern)


#for in range
for i in range(5): #range : 0부터 순서대로, list와 비슷한 성격
	print(i)

names =['철수','영희','지영','율규','동훈']
for i in range(len(names)):
	name = names[i]
	print(names[i])
	
for i,name in enumerate(names): #enumerate : 한번에 순서와 데이터값을 모두 가진다.
	print('{}번: {}'.format(i+1,name))
	
	
#print(chr(44032)
for i in range(11172):
		print(chr(44032+i),end='') #chr(44032) : 가


#모듈 사용하기
#import math -> math.pi, math.ceil, math.floor
#import random -> random.choice

#urllib.request의 url : http://꼭 써야된다.
def get_web(url):
	"""URL을 넣으면 페이지 내용을 돌려주는 함수"""
	import urllib.request
	response = urllib.request.urlopen(url)
	data=response.read()
	decoded=data.decode('utf-8')
	return decoded
	
url = input('웹 페이지 주소?')
print(get_web(url))
'''

#3.26 algorithm Question
def alternate(number): #string으로 생각할까?
	result=""
	list=[x for x in str(number)] #int(x)시에 '.' 인식 안됨
	if '.' in list:
		print('There is decimal points')
		index=list.index('.')
	else:
		print('There is not decimal points')
		index=len(list)
		
	#index=list.index('.') 
	#if not found, there is an error
	#find('.') : if found returns index, if not found return -1
	
	loop = 1
	halfResult = ""
	
	for i in range(index):
		print('i : {}, data : {}'.format(index-i-1,list[index-i-1]))
		halfResult = list[index-i-1] + halfResult
		if (loop%3 == 0) and (i !=index-1):
			halfResult =',' + halfResult
		loop =loop+1
	
	result = halfResult + str(number)[index:]
	print ('result : ',result)
		

#num=input()
alternate(123456.78)

	

