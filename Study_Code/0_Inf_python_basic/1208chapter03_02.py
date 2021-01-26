#chapter03-02
#파이썬 문자형
#문자형 중요

str1 = 'i am python'
str2 = "python"
str3 = """ppppp"""
str4 = '''dd'''

print(len(str1), len(str2), len(str3), len(str4))


#빈 문자열
str1_t1 = ''
str2_t2 = str()

# 이스케이프 문자
# i'm boy

print('I\'m boy') # 뒤에 있는 특수기호 그대로 표시
print('a \t b')
print('a \n b')
print('a \"\" b')
print('Do you have a \"time?\"')


t_s1 = "click \t start!"
t_S2 = "new line \n check!"

print(t_s1)
print(t_S2)

# raw string


 # 멀티라인 입력
# 역슬러시를 사용!



# 문자열 연산
str_o1 = "python" # 하나 하나를 리스트라고 생
str_o2 = "apple"
str_o3 = 'how are you doing?'
str_o4 = "seoul bucheon busan jeju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('p' in str_o2)
print('P' in str_o2)

# 문자열 형 변환

print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha)

print("Capitalize : ", str_o1.capitalize())
print("endswith :", str_o2.endswith("e"))
print("replace : ", str_o1.replace("thon", 'good'))
print("sorted : ", sorted(str_o3))
print("split : ", str_o4.split(' ')) # 특정 단어 문장 단위로 분리할 때

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) #__iter__

#출력

for i in im_str:
    print(i)


# 슬라이싱
str_sl = "Nice Python"

# 슬라이싱 연습

print(str_sl[0:3]) # 3 - 1 까지만 나옴 0 1 2
print(str_sl[5:]) # [5:11]
print(str_sl[:len(str_sl)-1]) #str_sl[:11]
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])

# 아스키 코드(또는 유니코드)

a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로
