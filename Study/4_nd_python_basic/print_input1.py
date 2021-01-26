# 표준 입출력

import sys

print('python', 'java', sep=' vs ')
print('python', 'java', sep=' , ', end='?') # end : 문장의 끝 부분을 변경 & 문장 한 줄로 붙임
print(' 무엇이 더 재밌을까요?')

print('python', 'java', file=sys.stdout) # 표준 출력
print('python', 'java', file=sys.stderr) # 표준 에러

# 시험 성적

scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items(): # .items() : 키와 밸류 쌍으로 나옴
    # print(subject, score)
    print(type(subject),type(score))
    print(subject.ljust(4), str(score).rjust(4), sep = ':') # ljust(8) : 8 개의 공간을 확보하고 왼쪽 정렬

# 은행 대기순번표
# 001, 002, 003
for num in range(1,21):
    print('대기번호 : ' + str(num).zfill(3))

# 표준 입력

answer = input('아무 값이나 입력하세요 : ')
print(type(answer)) # str으로 나옴, 항상 문자열로 저장됨
