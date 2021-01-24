# 파이썬 반복문
# for 실습

#코딩의 핵심
#for in <collection> -> 여러개를 포함 할 수 있는 튜플, 리스트, 딕셔너리
#    <loop body>

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

for v1 in range(10):
    print('v1 is :', v1)

print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)

print()

# 1 ~ 1000 합

sum1 = 0
for v in range(1, 1001):
    sum1 += v
print('1 ~ 1000 sum :', sum1)

print('1 ~ 1000 sum :', sum(range(1, 1001)))

print(type(range(1,11)))
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4,1001,4)))

# Iterables 반복할 수 있는 개체
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

#예제1

names = ['kim', 'park', 'cho', 'lee', 'choi', 'yoo']

for n in names:
    print('you are : ', n)



#예제2

lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("current number :", n)


# 예제3
word = "Beautiful"

for s in word:
    print('word : ', s)

print()
# 예제4
my_info = {
    "name": 'lee',
    "Age": 33,
    'city' : 'seoul'
}

for k in my_info:
    print('key :', my_info[k])
    print('key :', my_info.keys())

print()

for v in my_info.values():
    print('key :', v)


# 예제5
name = 'pineApple'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
         print('Found : 34!')
         break
    else:
        print('Not Found : ', num)

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]


for v in lt:
    if type(v) is bool:
        continue # -> bool 스킵을 시킴
    print('current type:', v, type(v))

# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print('Found : 24')
        break
else:
    print('Not Found : 24') # 반복후에도 없을 경우 else 구문 출력


# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()


# 변환 예제
name2 = 'aceman'

print('reversed', reversed(name2))
print('list', list(reversed(name2)))
print('tuple', tuple(reversed(name2)))
print('set', set(reversed(name2))) # 순서 x
