# 파이썬 튜플
# 리스트와 비교 중요
# 튜블 자료형(순서o, 중복o, 수정x, 삭제x) #불변


# 선언

a = ()
b = (1,)
c = (11, 12, 13, 14)
print(type(a), type(b))
d = (100, 1000, 'ace', 'base', 'captine')
e = (100, 1000, ('ace', 'base', 'captine'))

#인덱싱

print('>>>>>>>>>>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1] )
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 수정 x
# d[0] = 1500

#슬라이싱

print('>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])

# 튜블 연산
print('>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

#튜블 함수
a = (5, 2, 3, 1, 4)
print('a -', a)
print('a -', a.index(3))
print('a -', a.count(2))

#팩킹 & 언팩킹(packing, unpacking)

# 팩킹
t = ('goo', 'bar', 'aba', 'asdf')
print(t)
print(t[0])

# 언팩킹1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹1

t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
