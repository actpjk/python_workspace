# 주민등록번호
# 940703-11111111
# abcdef-11111111123

# 이메일 주소
# nadocoding@gmail.com
# nadocoding@gmail.com@gmail.com

# 차량 번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1
# 1000.2000.3333

# 자주 쓰이고 쉬운 부분만 실습.

import re # 정규식 사용 가능
# abcd, book, desk 
# ca?e 만 기억남
# care, cafe, case, cave, ...
# caae, cabe, cace, cade, ...

p = re.compile('ca.e') # 어떤 정규식을 할지 정해줌
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination | fade (x)
# $ (se$) : 문자열의 끝 > case, base | vet, fake (x)

# m = p.match('caffe')
# print(m.group()) # 매치되지 않으면 에러 발생

def print_match(m):
    if m:
        print('m.group():', m.group()) # 일치하는 문자열 반환
        print('m.string:', m.string) # 입력받은 문자열 반환
        print('m.start():', m.start()) # 일치하는 문자열의 시작 index
        print('m.end():', m.end()) # 일치하는 문자열의 끝 index
        print('m.span():', m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print('not matching!')

# m = p.match('careless') # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search('good care') # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall('good care cafe' ) # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)


# <정리>
# 1. p = re.compile('원하는 형태')
# 2. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search('비교할 문자열') : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 '리스트' 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination | fade (x)
# $ (se$) : 문자열의 끝 > case, base | vet, fake (x)









