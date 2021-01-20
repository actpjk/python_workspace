class Unit:
    def __init__(self):
        print('unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self) # 2. 따라서 다중 상속시에는 각 각 처리할 것
        Flyable.__init__(self)

dropship = FlyableUnit() # 1. 슈퍼 사용시 순서상 맨 마지막 상속 받는 클래스에 대해서만 init 함수가 호출됨.

