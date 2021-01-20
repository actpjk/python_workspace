# chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열 (시퀀스)
list : 리스트 (시퀀스)
tuple : 튜블(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입

str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10 == 10.0 false
int_v = 7
list = [str1, str2]
print(list)

dict = {
    "name": "Machine Learning",
    "version" : 2.0
}
tuple = (7, 8, 9)
set = {7, 8, 9}

print(type(str1))
print(type(str2))
print(type(bool))
print(type(int_v))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs() : 절대값
pow(x, y) x**y -> x의 y승
"""


#정수 선언
i = 77
i2 = -14
big_int = 312645987494465496789864894649848948949498489875646531658998

#정수 출력
print(i)
print(i2)
print(big_int)

#실수 출력
f = 0.312645987494465496789864894649848948949498489875646531658998
f2 = 3.141592
f3 = -3.9
f4 = 3/9

print(f)
print(f2)
print(f3)
print(f4)

#연산 실습

i1 = 39
i2 = 393
i3 = 9889489
i4 = 6412233131

f1 = 1.234
f2 = 3.939

print("f1 + f2 : ", f1 + f2)
print()

# 형 변환 실습

a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력

print(type(a), type(b), type(c), type(d))

#형 변환 핵심!

print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, False = 0
print(float(False))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5,3), 5**3)

# 외부 모듈

import math

print(math.ceil(5.1))
print(math.pi)
