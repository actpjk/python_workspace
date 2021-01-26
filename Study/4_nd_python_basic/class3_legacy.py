# <상속 & 다중 상속> 

# 일반 유닛
class Unit:
    def __init__(self, name, hp):  # __ini
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # self 는 자기자신 class에 self는 반드시 적어줌
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # name 과 hp 를 Unit에 던져 초기화 하고 damage 추가
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

firebat1 = AttackUnit('파이어뱃', 50, 20)
firebat1.attack('1시')

firebat1.damaged(25)
firebat1.damaged(25)

# <다중 상속> 부모 클래스를 2개 이상 상속 받음 ex) Unit 부모, AttackUnit 자식

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name, '3시')

