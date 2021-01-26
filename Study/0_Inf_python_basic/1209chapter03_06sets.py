# 집합 (set)
# 집합 (set) 자료형 (순서x, 중복x)

#선언
a = set([])
print(type(a))

b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'pen', 'cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'fodd', 'qux'} #-> 키없이 나열하면 셋임!
f = {42, 'foo', (1, 2, 3), 3.141234}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환 (set -> tuple)
t = tuple(b)
print('t - ', type(t))
print('t - ', t[0], t[1:3])

# 리스트 변환 (set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))


# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

print('s1|s2 : ', s1|s2)
print('s1|s2 : ', s1.union(s2))

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) #교집합이 있느 있으면 펄

# 부분 집합 확인
print('subset :',s1.issubset(s2)) # s1이 s2의 부분집합이냐
print('superset :',s1.issuperset(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)

s1.discard(7)    # -> 에러(예외)가 발생하지 않음.
print('s1 - ', s1)

s1.clear()
