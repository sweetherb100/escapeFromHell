'''
#모듈 만들기
def random_rsp():
    #무작위로 가위바위보를 낸다
    import random
    return random.choice(['가위','바위','보'])

PAPER='보'
SCISSOR='가위'
ROCK='바위'

#검색하기
import datetime,time
now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day)

#딕셔너리 만들기
#HashMap와 비슷한?
wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}

def rsp(mine,yours):
    if mine==yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else :
        return 'lose'

result = rsp('가위','바위')
print(result)

messages = {
    'win':'이겼다',
    'draw':'비겼다',
    'lose':'졌다'
}

print(messages[result])

#딕셔너리 수정하기
list = [1,2,3,4,5]
list[2]=33
list.append(6)

dict = {
    'one':1,
    'two':2
}
dict['one']=11
dict['three']=3 #list는 append, dict는 그냥 바로 추가 가능
print(dict)
del(dict['one'])
print(dict)
print(list.pop(0)) #지우면서 첫번재 index 값 나옴

print(list)
print(dict.pop('two')) #지우면서 첫번재 index 값 나옴
print(dict)

#바꾸기와 지우기는 dict, list 똑같은 문법. 값 추가만 다르다

#딕셔너리와 반복문
seasons=['spring','summer','autumn','winter']
for season in seasons:
    print(season)

ages={'Tod':35,
      'Jane':23,
      'Paul':62
      }

for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)

for key in ages:
    print('{}의 나이는 {}입니다.'.format(key, ages[key]))

for key, value in ages.items(): #list에서 enumerate와 비슷
    print('{}의 나이는 {}입니다.'.format(key, value))
#dict : list와 다르게 순서 보장 안됨. 따라서 순서가 중요하면 list 사용

#리스트와 비교
list = [1,2,3,4,5]
dict={'one':1, 'two':2}
#값 불러오기
list[0]
dict['one']

#값 삭제
del(list[0])
list.remove(1)
del(dict['one'])

#length
len(list)
len(dict)

#값 있는지 확인
2 in list
#false
'two' in dict.keys()
#True
'to' in dict.keys()
#False
2 in dict.values()
#True

#값 지우기
list.clear()
dict.clear()

list = [1,2,3,4,5]
dict= {'one':1,'two':2}
#pop
list.pop(0)
dict.pop('one')

#결합
big_list=[1,2,3]+[4,5,6]
dict1={1:100,2:200}
dict2={1:1000, 3:300}
dict1.update(dict2)
print(dict1)

dict1={1:100,2:200}
dict2={1:1000, 3:300}
dict2.update(dict1)
print(dict2)

#튜플 만들기 (순서가 정해진 값의 집합)
list1 =[1,2,3,4,5]
print(type(list1))
tuple1=(1,2,3)
print(type(tuple1))
tuple2=1,2,3
print(type(tuple2))
tuple3 = tuple(list1)
print(tuple3)

#값 가져오기
print(tuple3[0])

#값 바꾸기
#tuple3[0] = 5
#값을 한번 만들면 값을 바꾸지 못한다. 에러발생
#삭제, 팝도 에러발생


#(튜플을 이용한) packing, unpacking
#함수의 리턴값으로 여러개의 값을 전달할수있다.
#packing : 하나의 변수에 여러개의 변수를 넣는것
#unpacking : packing 된 값에서 여러개의 변수를 꺼내오는 것
a,b=1,2
print(a)
print(b)
#a,b라는 하나의 튜플 생성. 1,2 라는 하나의 튜플 생성. =을 통해 대입

c=(3,4)
print(c)
d,e=c
print(d)
print(e)
#c의 값을 unpacking해서 d,e의 값에 넣음

f=d,e
print(f)
#변수 d,e를 f의 값에 packing

x=5
y=10
#x와 y의 값을 바꾸려면 보통 temp쓰는데
x,y=y,x
print(x)
print(y)

def tuple_func():
    return 1,2

q,w=tuple_func()
print(q)
print(w)

#튜플을 이용한 함수의 리턴값
list = [1,2,3,4,5]
for i,v in enumerate(list):
    print('{}번째 값 : {}'.format(i,v))
#방식 : tuple로 값을 return해줘서 한번에 i,v라는 변수에 저장

for a in enumerate(list):
    print('{}번째 값 : {}'.format(a[0],a[1]))

for a in enumerate(list):
    print('{}번째 값 : {}'.format(*a))

ages={'Tod':35,
      'Jane':23,
      'Paul':62}

for key,val in ages.items():
    print('{}의 나이는 : {}'.format(key,val))
#그런데 꼭 이렇게 2개의 변수로 받을 필요없고 1개의 변수로 받아도된다.

for a in ages.items():
    print('{}의 나이는 : {}'.format(a[0],a[1]))

for a in ages.items():
    print('{}의 나이는 : {}'.format(*a))


#while문 쓰기
selected = None #selected에 아무 값이 없다는 의미
#while selected not in ['가위','바위','보']:
#    selected=input('가위, 바위, 보 중 선택하세요>')

#print('선택된 값은 : ',selected)

patterns = ['가위','바위','보']
for pattern in patterns:
    print(pattern)

for i in range(len(patterns)):
    print(patterns[i])


length=len(patterns)
i=0
while i<length:
    print(patterns[i])
    i=i+1


#break,continue
list = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    if i%3==0:
        continue #중요한 로직을 깊은 block에 안들어가게 함으로써 어떤 블럭이 중요한 부분인지 분리해줌
    print(i)
    print(i)


#try except
# list=[]
# list[0] #IndexError

# text='abc'
# number=int(text) #ValueError

text = '100%'
try:
    number=int(text)
except ValueError:
    print('{}는 숫자가 아니네요.'.format(text))

def safe_pop_print(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3],5)


#예외의 이름을 모를 때
try:
    list = []
    print(list[0])

except Exception as ex:
    print('에러가 발생하였습니다',ex)


#raise (에러를 직접 일으키는 방법)
def rsp(mine,yours):
    allowed=['가위','바위','보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError

try :
    rsp('가위','바') #try, except 안쓰면 Errror 발생
except ValueError:
    print('잘못된 값을 넣은 것 같습니다')

school = {'1반':[172,185,195,177,165,199],
          '2반':[165,177,167,180,191]
          }

try:
    for class_number, students in school.items():
        for student in students:
            if(student>190):
                print(class_number,'반에 190을 넘는 학생이 있습니다')
                raise StopIteration #바로 for loop 멈추고 싶을때, 일단 일부러 error를 발생하고 except 처리
except StopIteration:
    print('항상종료')


#논리연산 더 알아보기
a=10
if a<0 and 2**a >1000 and a%5==2 and round(a) == a:
    print('복잡한 식')

def return_false():
    print('함수 return false')
    return False

def return_true():
    print('함수 return true')
    return True

a=return_false()
b=return_true()

if a and b:
    print(True)
else:
    print(False)

#단락평가 (파이썬에서 지원!!!!)
# if return_false() and return_true(): 일때
# return_true()함수 자체가 실행되지 않는다. 어차피 return_false()에서 false return하기 때문에
#단락평가 안하면 Error를 뱉을수있는데 때에 따라서 안뱉는다.
# ex) dict ={"Key2":"Value2"}
# if "Key1" in dict and dict["key1"]="Value1"


#bool값과 논리연산
print(bool(0)) #F
print(bool(1)) #T
print(bool(-1)) #T
print(bool([])) #F
print(bool([3])) #T
print(bool(None)) #F
print(bool('')) #F
print(bool('Hi')) #T
#단락평가에서 활용 가능

#************단락평가로 이해하기 
#input 아무 것도 안쓰면 False로 return, 입력을 하면 True가 되면서 뒤에 부분 ('아무것도 못받았어')는 아예 무시

value=input('입력해주세요>') or '아무것도 못받았어'
print('입력받은 값>',value)
#***********or연산의 결과는 앞의 값이 True이면 앞의 값을. 앞의 값이 False이면 뒤의 값을 따른다


#List의 다양한 기능
list1=[135,462,27,2753,234]
#print(list.index(27))
#print(list.index(22)) #index 값없으면 Error 발생. if절로 있는지 확인 후 사용

list2=[1,2,3]+[4,5,6]
print(list2)
list1.extend([9,10,11]) #+해도 상관없는데 성능이 약간 더 좋음
print(list1)
list1.insert(2,999) #첫번째 값은 insert할 index
print(list1)
list1.insert(-2,888) #-는 뒤에서 index
print(list1)
list1.insert(100000,777) #range 밖이면 가장 마지막 index에 추가
print(list1)

list1.sort()
print(list1)
list1.reverse()
print(list1)


#List와 문자열
my_list=[1,2,3,4,5,6]
my_list[0]
my_list[1]
str="Hello World"
str[0]
str[1]

3 in my_list
9 in my_list
"H" in str
"Z" in str

#*****list(문자열-> List화), split, join (리스트->문자열) 활용
characters = list("abcdef")
print(characters)
words="Hello Word는 프로그래밍을 배우기에 아주 좋은 사이트 입니다."
words_list= words.split() #param 없으면 default로 " "를 기준으로 split
print(words_list)
print(" ".join(words_list))


#Slice
text="hello World"
#리스트의 일부분을 썰어서 가져온다
print(text[1:5])
print(text[:2])

list=['g','f','e','d','c','b','a']
print(list[1:3])
print(list[:2])
print(list[2:])

#list2=list 이렇게 할 경우, list2도 sort되어서 나옴
list2=list[:] #list[:]는 list 복사한 개념. 따라서 list2, list 별도로 나온다
list.sort()
print(list2)
print(list)


#Slice의 step
list1=list(range(20))
print(list1)
print(list1[5:15])
print(list1[5:15:2]) #2개 걸러서 가져오고 싶을떄 ('step') 음수값도 가질수있다.
print(list1[5:15:-1]) #이렇게 쓰면 안됨
print(list1[15:5:-1]) #step 음수도 가능
list[::3]
list[::-3]


#Slice로 리스트 수정하기
numbers = [0,1,2,3,4,5,6,7,8,9]
numbers =list(range(10))
del numbers[0]
print(numbers)

del numbers[:5]  #slice를 이용해 영역지정해서 지울 수 있다.
print(numbers)

numbers[1:3]=[77,88,99]
print(numbers)

numbers[1:4]=[8] #꼭 리스트화 해서 넣기
#slice를 이용하여 영역을 한번에 바꾸기
print(numbers)
'''
