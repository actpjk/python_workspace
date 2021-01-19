# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'kim', 'phone': '01055555555', 'birth': '940703'}
b = {0: 'hello python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'status': True
}

f = dict(
    Name='niceman',
    City='Seoul',
    Age='33',
    Grade='A',
    Status=True
) # -> bset

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('f - ', type(f), f)
print('f - ', type(list(f))

# 출력

# print('a - ', a['name']) # 키 존재 x 시 에러 발생
# print('a - ', a.get('name')) # -> best 키 존재 안하면 none으로 표시됨 더 안전
# print('b - ', b[0])
# print('b - ', b.get(0))
# print('f - ', f.get('City'))


# # 딕셔너리 추가
# a['address'] = 'seoul'
# print('a - ', a)
# a['rank'] = [1, 2, 3]
# print('a - ', a)


# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용가능
print('='*100)
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('='*100)
print()
print('='*100)
print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('='*100)
print()
print('='*100)
print('a - ', a.items())
print('a - ', list(a.items()))
print('='*100)
print()
print('='*100)
print('a - ', a.pop('name'))
print('a- ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print('f - ', f.popitem())
print('f -' , f)
print('f - ', f.popitem())
print('f -' , f)
print('f - ', f.popitem())
print('f -' , f)

print()

print('a - ', 'birth' in a)
print('d - ', 'city' in d)

a['test'] = 'test_dict'

print()

# 수정, 추가
a['test'] = 'test_dict'
a.update(birth='910904')
print('a - ', a)
