'''
#자료형 다루기
e="Hello World"
print(type(e))
print(type(42.0))
print(type(4))
print(isinstance(42,int))


#인스턴스 이해
number1=[]
print(type(number1))
numbers2= list(range(10))
print(numbers2)
chars = list("hello")
print(chars)

print(isinstance(number1,list))


#클래스 만들기
class Human():
    #사람
#여기까지가 class (빈 클래스)

person1 = Human()
person2 = Human()
person1.language = '한국어'
person2.language = 'English'
print(person1.language)
print(person2.language)
person1.name ='서울시민'
person2.name ='김지영'

def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name, person.language))
    
speak(person1)
speak(person2)

#또는
#person1.speak = speak #이렇게 쓰면 안됨...
#person1.speak(person1)으로 하면 되긴됨
#person2.speak= speak #이렇게 쓰면 안됨...

Human.speak = speak
person1.speak()
person2.speak() #괄호를 써야지 함수를 실행하는 것처럼 되니까 써야되는듯
#근데 왜 인자를 안받아도 되는건지는 의문...


#모델링 (클래스로 현실을 반영하기)
class Human():
    #인간

person = Human()
person.name = '철수'
person.weight=60.5
#이렇게 매번 하기에 번거로움.

def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight=weight
    return person

person=create_human("철수",60.5)
print(person.weight)

Human.create=create_human
person=Human.create("철수",60.5)
print(person.weight)

def eat(person):
    person.weight+=0.1
    print("{}가 먹어서 {}kg가 되었습니다".format(person.name, person.weight))

def walk(person):
    person.weight -= 0.1
    print("{}가 걸어서 {}kg가 되었습니다".format(person.name, person.weight))

Human.eat =eat
Human.walk = walk

person.walk()
person.eat()
person.walk()


#메소드 이해하기
class Human():
    #인간


def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight=weight
    return person
Human.create=create_human

def eat(person):
    person.weight+=0.1
    print("{}가 먹어서 {}kg가 되었습니다".format(person.name, person.weight))

def walk(person):
    person.weight -= 0.1
    print("{}가 걸어서 {}kg가 되었습니다".format(person.name, person.weight))

Human.eat =eat
Human.walk = walk

person=Human.create('철수',60.5)
person.walk()
person.eat()
person.walk()
#하지만 번거로움. 따라서 class 안에 함수를 넣어버리기 -> 메소드

class Human():
    #인간

    def create(name, weight):
        person = Human()
        person.name = name
        person.weight=weight
        return person

    def eat(person):
        person.weight+=0.1
        print("{}가 먹어서 {}kg가 되었습니다".format(person.name, person.weight))

    def walk(person):
        person.weight -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다".format(person.name, person.weight))

person = Human.create("철수",60.5)


class Human():
    #인간
    def create(name, weight):
        person = Human()
        person.name = name
        person.weight=weight
        return person

    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg가 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다".format(self.name, self.weight))

    def speak(self,message):
        print(message)


person = Human.create("철수", 60.5)
#eat(person) #에러 남
person.eat() #에러 안남 -> person이 eat의 매개변수 self로 인자를 넘겨주기 때문에

person.speak("안녕하세요")


#특수한 메소드

class Human():
    #인간
    def __init__(self):
        print('init 실행')

    def __init__(self,name,weight):
        print('init 실행2')
        print('이름은 {}, 몸무게는{}'.format(name,weight))
        self.name =name
        self.weight= weight

    def __str__(self):
        print('문자열화 함수')
        return "{} 몸무게 {}kg".format(self.name, self.weight)

    def create(name, weight):
        person = Human()
        person.name = name
        person.weight=weight
        return person

    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg가 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다".format(self.name, self.weight))

    def speak(self,message):
        print(message)


# person2 = Human() #생성자 1개만 해야하나보다?!?!
person=Human("철수",50)
print(person) #인스턴스 출력시에 __str__ 함수 호출 (Human을 string으로 표현할때 사용)
print(person.name)
print(person.weight)


#상속
class Animal(): #부모 class
    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')

class Human(Animal): #상속. 자식 클래스
    def wave(self):
        print('손을 흔든다')

class Dog(Animal): #상속. 자식 클래스
    def wag(self):
        print('꼬리를 흔든다')


person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()


#단순 오버라이드 (override)
class Animal(): #부모 class
    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')

    def greet(self):
        print('인사한다')

class Human(Animal): #상속. 자식 클래스
    def wave(self):
        print('손을 흔든다')

    def greet(self): #override
        self.wave()

class Dog(Animal): #상속. 자식 클래스
    def wag(self):
        print('꼬리를 흔든다')

    def greet(self): #override
        self.wag()

person = Human()
person.greet()

dog = Dog()
dog.greet()


#super()
class Animal(): #부모 class
    def __init__(self,name):
        self.name = name

    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')

    def greet(self):
        print('{}가 인사한다'.format(self.name))

class Human(Animal): #상속. 자식 클래스
    def __init__(self,name,hand):
        super().__init__(name)
        self.hand=hand

    def wave(self):
        print('{}손을 흔들면서'.format(self.hand))

    def greet(self): #override
        self.wave()
        super().greet() #super에 꼭 괄호!!!! super()


person=Human("지영이","오른")
person.greet()


#내 예외 만들기
from Python.unexpectedException import UnexpectedRSPValue
from Python.unexpectedException import BadUserName
from Python.unexpectedException import PasswordNotMatched

value = '가'

try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print("에러가 발생했습니다.")


def sign_up():
    

try:
    sign_up()
except BadUserName:
    print("이름으로 사용할 수 없는 입력입니다.")
except PasswordNotMatched:
    print("입력한 패스워드가 서로 일치하지 않습니다.")

# def sign_up():
#     
#
# try:
#     sign_up()
# except BadUserName:
#     print('이름으로 사용할 수 없는 입력입니다')
# except PasswordNotMatched:
#     print('입력한 패스워드가 서로 일치하지 않습니다')


#List Comprehension
areas =[]
for i in range(1,11):
    if i%2==0:
        areas=areas+[i*i] #areas에 따로 index 없어도 append 형식으로 되나보다. plus때문에 그런가?

print(areas)

#이것보다 훨씬 간단하게 할수 있다! 한줄로!!
areas2=[ i*i for i in range(1,11) if i%2==0] #이런 형식이 Comprehension
print(areas2)

#이중 for loop도 가능 (각 좌표를 tuple로 가진다.)
print([(x,y) for x in range(15) for y in range(15)])


#Dictionary (zip 명령어 활용)
students=['태연','진우','정연','하늘','성진']
# for number, name in enumerate(students):
#     print('{}번의 이름은 {}입니다'.format(number,name))

students_dict={"{}번".format(number+1):name for number,name in enumerate(students)} #Dictionary Comprehension
print(students_dict)

scores =[35,26,7,2,85]
for x,y in zip(students,scores):
    print(x,y)

score_dic ={student:score for student,score in zip(students,scores)}
print(score_dic)


#datetime
import datetime
start_time = datetime.datetime.now()
print(type(start_time))
tobe_time = start_time.replace(year=2018, month=2, day=1,second=10)
print(tobe_time)
tobe_time2 =datetime.datetime(2015,2,1)
print(tobe_time2)

how_long = tobe_time-datetime.datetime.now()
type(how_long)
print(how_long)
print(how_long.days)
print(how_long.seconds) #tobe_time에 second가 없으면 how_long.seconds가 0으로 나옴
'''

#timedelta
import datetime
hundred = datetime.timedelta(days=100)
print(hundred)
print(datetime.datetime.now() + hundred)

hundred_before = datetime.timedelta(days=-100)
print(datetime.datetime.now() + hundred_before)
print(datetime.datetime.now() - hundred)

tomorrow = datetime.datetime.now().replace(hour=9,minute=0,second=0) + datetime.timedelta(days=1)
print(tomorrow)











