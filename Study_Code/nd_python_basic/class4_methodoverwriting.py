# <메소드 오버라이딩> : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것.

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  # __ini
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # self 는 자기자신 class에 self는 반드시 적어줌
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # name 과 hp 를 Unit에 던져 초기화 하고 damage 추가
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

# <다중 상속> 부모 클래스를 2개 이상 상속 받음 ex) Unit 부모, AttackUnit 자식

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'\
            .format(name, location, self.flying_speed))

# 메소드 오버라이딩, 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 메소드 오버라이딩
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

marine = AttackUnit('마린', 50, 3, 2)
marine.damaged(5)

valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name, '3시')

vulture = AttackUnit('벌쳐', 80, 10, 20)

battlecruiser = FlyableAttackUnit('배틀 크루저', 300, 50, 10)

vulture.move('11시')
#battlecruiser.fly(battlecruiser.name, '9시')  # move, fly 계속 변경해줘야하는게 너무 귀찮음 -> 오버라이딩 사용
battlecruiser.move('9시')

# < pass >

# 건물

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit('서플라이디폿', 550, '7시')

def game_start():
    print('게임이 시작됐습니다.')

def game_over():
    pass

game_start()
game_over()

# < super >

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # 셀프 없이 부모 클래스 사용 초기화.
        self.location = location
        