# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lamda)

# 함수 정의 방법
# def function_name(parameter):
#   code


#예제1

def first_func(w):
    print("hello, ", w)

word = "goodboy"

first_func(word)

# 예제2

def return_func(w1):
    value = "hello, " + str(w1)
    return value

x = return_func('Goodboy2')
print(x)


# 예제3 (다중반환) -> 함수형 프로그래밍 꼭 공부해볼 것.

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x, y, z)

# 튜블 리턴

def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(type(q), q)


# 리스트 리턴

def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul3(20)
print(type(p), p)
print()

# 딕셔너리 리턴

def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2':y2, 'v3':y3}

d = func_mul4(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())


# 중요
# *args, **kwargs

print('*args(언팩킹)')

def args_func(*d): # 매개변수 명 자유
    for i, v in enumerate(d):
        print('result : {}'.format(i), v)
    print('------------')

args_func('Lee')
args_func('Lee', 'park')
args_func('lee', 'park', 'kim')


print('**kwargs(언팩킹)')

def kwargs_func(**kwargs): # 매개변수 명 자유, 키와 밸류인 것을 매개변수로 넘길 때 사용한다.
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-------------')

kwargs_func(name1 = 'lee')
kwargs_func(name1 = 'lee', name2 ='park', name3 ='cho', sendSMS=True)


# 전체 혼합

def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'lee', 'kim', 'park', age1 = 20, age2 = 30, age3 = 25)

# 중첩 함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)
nested_func(100)
print('_-------------------------')
# 실행불가
# func_in_func(1000)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

#def mul_func(x, y):
#    return x * y

#lambda x, y: x*y


# 일반 함수 -> 변수 할당
def mul_func(x, y):
    return x * y
print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20,50))

#람다 함수 -> 할당
lambda_mul_func = lambda x, y : x * y
print(lambda_mul_func(50, 50))

def func_final(x, y, func):
    print('>>>>>', x * y * func(100,100))

func_final(10, 20, lambda x, y : x * y)
