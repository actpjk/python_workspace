# chapter02-1
# 파이썬 완전 기초 과정
# 프린트 사용법

# 기본 출력
print('python start')
print('''python''')
print("""python""")



# separator 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('010', '7777', '1325', sep='-')
print('python', 'google.com', sep=' @ ')

print()

# end 옵션

print('welcome to', end=' ')
print('it news', end='')
print('web site')

# file 옵션

import sys
print('learn python', file=sys.stdout)
print()

# format 사용(d : 3, s : 'python', f : 3.141592)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', '2'))
print('{1} {0}'.format('pp', 'wef'))
print('{2} {0} {1}'.format('2', '3', '5'))

print('{0} {2} {1}'.format('1', '3', '6'))

# %s

print('%10s' % ('nice111')) #print('%10s' % (nice111))
print('%10s' % ('officeidd'))
print('{:>10}'.format('nice')) #print('{:>10}'.format('nice'))


print('%-10s' % ('nice111'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstucy'))

print('{:10.5}'.format('pythonstudy'))


# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f

print('%1.18f' % (3.145498412))
print('{:f}'.format(3.16465464))

print('%06.2f' % (3.14549842))
print('{:06.2f}'.format(3.156446984))


print('%.5s' % ('niceeeeeee'))
print('%.5s' % ('pythonstucyeeee'))

print('{:10.5}'.format('pythonstudyeeeee'))
