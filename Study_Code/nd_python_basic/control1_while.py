# while문

customer = '토르'
index = 5
while index >= 1:
    print('{0},  커피가 준비 되었습니다. {1} 번 남았어요.'.format(customer, index))
    index -= 1
    if index == 0:
        print('커피 아웃입니다.')

customer = '아이언맨'
index = 1
while True:
    print('{0},  커피가 준비 되었습니다. 호출 {1} 회.'.format(customer, index))
    index += 1

customer = '토르'
person = 'unknown'

while person != customer : # person이 customer 가 아니라면 계속 반복
    print('{0},  커피가 준비 되었습니다.'.format(customer))
    person = input('이름이 어떻게 되세요?')