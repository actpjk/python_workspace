# 파이썬 반복문
# while 실습

# while <expr>: if 문과 사용이 똑같으나 반복이 만족될 때까지 계속 반복
#   <statements(s)>

#예제1

n = 5
while n > 0:
    print(n)
    n = n - 1

# 예제2

a = ['foo', 'bar', 'bza']

while a:
    print(a.pop(-1)) # last in first out


# 예제 3
# break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2 :
        break
    print(n)
print('loop end')

# 예제4

m = 5
while m > 0:
    m -= 1
    if m == 2 :
        continue
    print(m)
print('loop end')

# 예제5

i = 1

while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1


#예제 6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')    # 와일문도 브레이크가 없다면 엘즈문을 한 번 실행됨.

# 예제 7

a = ['foo', 'var', 'les', 'par']
b = 'sadlfj'

i = 0
while i < len(a):
    if a[i] == b:
        break
    i += 1
else: print(b, 'not found')

# 무한반복

# 예제8

a = ['foo', 'var', 'les']


while True:
    if not a:
        break
    print(a.pop())
