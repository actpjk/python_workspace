# <메소드>

class Unit:
    def __init__(self, name, hp, damage):  # __ini
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{} 유닛 생성'.format(name))
        print('체력 {}, 공격력 {}\n'.format(hp, damage))

class AttackUnit: # self 는 자기자신 class에 self는 반드시 적어줌
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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


