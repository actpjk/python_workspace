#파이썬 리스트
#자료구조에서 중요
#리스트 자료형(순서o, 중복o, 수정o, 삭제o)


# 선언
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85] #len
print(len(c))
d = [1000, 10000, 'ace', 'base', 'captine']
e = [1000, 10000, ['ace', 'base', 'captine']]
f = [21.42, 'foodf', 3, 4, False, 3.141592]

print(d[1]+d[0])


#인덱싱(원하는 데이터를 꺼내오는 과정)

print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[1] + d[0] + d[1])
print('d - ', d[-1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])


# 리스트 연선
print('>>>>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'test' + c[0]", 'test' + str(c[0]))

# 값 비교

print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()
# identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>>>>>>')

c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c -', c)
c[1] = ['a', 'b', 'c'] #하나의 리스트 안에 또 리스트 -> 중첩.
print('c -', c)
c[1:3] = []
print('c -', c)
del c[2]
print('c - ', c)


# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a -', a)

a.append(10) #끝 부분에 삽입하는 함수
print('a -', a)

a.sort() # 오름차순 정렬
print('a -', a)

a.reverse() # 내림차순 정렬
print('a -', a)

print('a - ', a.index(3))

a.insert(2, 7)
print('a -', a)

# del a[6484]

a.remove(10)
print('a -', a)
print('a - ', a.pop())
print('a -', a)
print('a - ', a.pop())
print('a -', a)
print('a - ', a.count(4))

ex = [8, 9]
a.extend(ex)
print('a -', a)


print('a - ', a.index(3), a[3])
# 삭제 : remove, pop, del

#반복문 활용

while a:
    data = a.pop() #pop 끝부부분에 있는 값을 꺼내온다.
    print(data)
