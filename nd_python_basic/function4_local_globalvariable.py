# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))
    return gun # 변경된 값을 외부로 던짐

print('전체 총 : {0}'.format(gun))
gun = checkpoint_return(gun, 4) # 4 명 경계 근무
print('남은 총 : {0}'.format(gun))