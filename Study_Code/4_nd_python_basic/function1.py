# 함수는 정의만 해줌

def open_account():
    print('새로운 계좌가 생성되었습니다.')

open_account()

def deposit(balance, money):
    print('입금이 완료 되었습니다. 잔액은 {0} 원 입니다.'.format(balance + money))
    return balance + money # 반환

def withdraw(balance, money):
    if balance >= money:
        print('출금이 완료 되었습니다. 잔액은 {0} 원 입니다.'.format(balance - money))
        return balance - money
    else:
        print('출금 안됩니다. 잔액은 {0} 원 입니다.'.fromat(balance))
        return balance
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission # 튜플 형식으로 보내줌

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)

# balance에 1000원 저장됨
balance = deposit(balance, 1000)
print(balance)

commission, balance = withdraw_night(balance, 500)
print('수수료는 {0} 원이며, 잔액은 {1} 원입니다.'.format(commission, balance))
