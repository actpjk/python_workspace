#chapter02-2
#파이썬 완전 기초
#파이썬 변수

#기본 선언
n = 700

#출력
print(n)
print(type(n))

#동시 선언

x = y = z =700

print(x, y, z)

#선언

var = 75

#재선언

var = 'change value'

print(type(var))
print(var)

#object references
#변수 값 할당 상태



print(300)
print(int(300))




#예1)
print(300)


m = 800
n = 655

print(id(m))
print(id(n))
print()
print(id(m) == id(n))


m = 8000
n = 8000

print(id(m))
print(id(n))
print()
print(id(m) == id(n))

# 다양한 변수 선언
# camel case : numberOfCollegeGraduates -> Method
# pascal case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates

# 허용하는 변수 선언 법

age = 1
Age = 1
a_g_e = 1
_age = 5
age_ = 7
_AGE_ = 4


# 예약어는 변수명으로 불가능
# class, as, for 등
