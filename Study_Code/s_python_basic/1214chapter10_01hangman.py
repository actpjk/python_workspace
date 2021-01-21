# 행맨 미니 게임 제작(1)
# 기본 프로그램 제작 및 테스트

import time


# 처음 인사

name = input("what is your name?")

print("hi, " + name, "time to play hangman game!")

print()

time.sleep(1)

print('start loading...')
print()
time.sleep(0.5)

# 정답 단어
word =  "secret"

# 추측 단어

guesses = ''

# 기회
turns = 10

# 핵심 while
# 찬스 카운트가 남아 있을 경우

while turns > 0:
    # 실패 횟수
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')
        else:
            #틀린 경우 대시로 처리
            print('_', end=' ')
            failed += 1
    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        print('congratulations! the guesses is correct.')
        # while 구문 중단
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    guess = input('guess a character.')

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        # 기회 횟수 감소
        turns -= 1
        # 오류 메세지
        print('Oops! Wrong')
        # 남은 기회 출력
        print('you have', turns, 'more guesses!')

        if turns == 0:
            # 실패 메세지
            print('your hangman game failed. bye!')
