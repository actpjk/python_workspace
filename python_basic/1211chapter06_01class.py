# 파이썬 클래스(붕어빵 틀)
# oop(객체(소프트웨어로 구현할 대상) 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 지정된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1

class Dog2: # object 상속 받음
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog2)

# 인스턴스화(설계도를 바탕으로 구현된 것 인스턴스, 코드로 직접 작성해서 구현된 것)
a = Dog2('cloud', 2)
b = Dog2('kung', 4)
c = Dog2('cloud', 2)

# 비교

print(a == b, id(a), id(b))

# 네임스페이스

print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.age))


print(Dog2.species)
print(a.species)
print(b.species)

#예제 2
# self의 이해
class selftest:
    def func1(): # 클래스 메소드
        print('func1 called')
    def func2(self): # 인스턴스 메소드
        print(id(self))
        print('func2 called')

f = selftest()

#print(dir(f))

print(id(f))

# f.func1() # 예외
f.func2()

selftest.func1()
selftest.func2(f)
# selftest.func2() 예외

# 예제3
# 클래스 변수, 인스턴스 변수

class warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        self.name = name
        warehouse.stock_num += 1


    def __del__(self):
        warehouse.stock_num -= 1

user1 = warehouse('lee')
user2 = warehouse('cho')

print()

print(warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', warehouse.__dict__)
print('---------', user1.stock_num)

del user1
print('after', warehouse.__dict__)

# 예제4

class Dog: # object 상속 받음
    # 클래스 속성
    species = 'firstdog'
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)


# 인스턴스 생성
c = Dog('july', 4)
d = Dog('bee', 10)

print(c.info())
print(d.info())
print(c.speak('Wal Wal'))
print(d.speak('mimi'))
