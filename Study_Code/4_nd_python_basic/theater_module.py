# 모듈 필요한 것 들끼리 부품처럼 만드는 것을 모듈화, 함수나 클래스를 담고 있는 것. 확장자가 .py

# 일반 가격
def price(people):
    print('{0}명 가격은 {1}원 입니다.'.format(people, people * 10000))

# 조조 할인 가격
def price_morning(people):
    print('{0}명 조조 할인 가격은 {1}원 입니다.'.format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print('{0}명 군인 할인 가격은 {1}원 입니다.'.format(people, people * 4000))