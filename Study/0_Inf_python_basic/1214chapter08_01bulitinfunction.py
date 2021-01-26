# 파이썬 내장 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습
#
# 절대값
# abs()

print(abs(-3))

# all, any : iterable 요소 검사(참, 거짓)

print(all([1, 2, 3, ''])) # and
print(any([1, 2, 0])) # or

# chr : 아스키 -> 문자, ord : 문자 -> 아스키

print(chr(87))
print(ord('W'))

# 중요! enumerate : 인덱스 + iterable 객체 생성

for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i+1, name)

# 중요! filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# id : 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

# len : 요소의 길이 반환

print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))

# max, min : 최대값 최소값

print(max([1, 2, 3]))
print(max('python study'))
print(min([1, 2, 3]))
print(min('pythonstudy'))

# 중요! map : 반복가능한 객체 요소를 지정한 함수를 실행 후에 추출함.
def conv_abs(x):
    return abs(x)
print(list(map(conv_abs, [1, -3, 2, 0 ,-5, 6])))
print(list(map(lambda x: abs(x), [1, -3, 2, 0 ,-5, 6])))

# pow : 제곱값을 반환한다.

print(pow(2, 10))

# range : 반복 가능한 객체(iterable)를 반환한다.
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

# round : 반올림 함수

print(round(6.51242, 2))
print(round(5.4))

# sorted : 반복 가능한 객체(iterable)를 정렬 후 반환

# list, tuple, dictionary, set 은 반드시 외우자

print(sorted([6,7,5,3,2,77]))

a = sorted([6,7,5,3,2,77])
print(a)
print(sorted(['p','y','t','h','o','n']))

# sum : 반복 가능한 객체(iterable)의 합을 반환

print(sum(range(1,100)))

# type : 자료형 확인

print(type(3))
print(type({}))
print(type([]))
print(type(()))

# zip : 반복가능한 객체(iterable)의 요소를 묶어서 반환

print(tuple(zip([10,20,30], [40,50,60])))
print(type(list(zip([10,20,30], [40,50]))[0]))
