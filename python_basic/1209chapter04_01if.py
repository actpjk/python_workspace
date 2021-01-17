# 파이썬 제어문
# if 실습


# 기본 형식
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


print(type(True)) # m 0이 아닌 수, "abc", [1,2,3,..] (1,2,3,...)
print(type(False)) # 0, "", [], {}, (),....


#예1
# 파이썬은 정확하게 들여쓰기를 해줘야함.
if True:
    print('good')

if False:
    print('bad')

# 예2

if False:
    print('bad!')
else:
    print('good!')

# 관계 연산자
# > >= < <= == !=

x = 15
y = 10

print(x == y)

print(x !=  y)

print(x > y)
print(x < y)

#예3
city = ""
if city:
    print("you are in:", city)
else:
    print("please enter your city")

#예4
city2 = "seoul"
if city2:
    print("you are in:", city)
else:
    print("please enter your city")


# 논리연산자(중요)
# and, or, not

a = 75
b= 40
c= 10

print('and : ', a > b and b < c)
print('or : ', a > b or b < c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리

print('el :', 3+12 > 7+3)
print('el : ', 5+3*10 > 7+3*20)
print('el : ', 5+10 > 3 and 7+3 == 10 )

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fall')

id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')


if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')



#예6
#다중조건문


num = 75

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

#예7
# 중첩 조건문

grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')


# in, not in

q = [10, 20, 30]
w = [70, 80, 90, 100]
e = {'name' : 'lee', 'city': 'seoul', 'grade': 'A'}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print('seoul' in e.values())
