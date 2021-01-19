# <class> & <멤버 변수>

# name = '마린'
# hp = 40
# damage = 5

# print('{} 생성'.format(name))
# print('체력 {}, 공격력 {}\n'.format(hp, damage))

# tank_name = '탱크'
# tank_hp = 150
# tank_damage = 35

# print('{} 생성'.format(tank_name))
# print('체력 {}, 공격력 {}'.format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(\
#         name, location, damage))

# attack(name, '1시', damage)
# attack(tank_name, '1시', tank_damage)

# 만약 탱크가 하나 더 추가된다면? -> 유닛이 수십 수백이면 힘들다. 그래서 class 필요 
# 붕어빵 틀에 비교. class 도 하나의 틀 연관있는 변수와 함수의 집합.

class Unit:
    def __init__(self, name, hp, damage):  # __ini
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{} 유닛 생성'.format(name))
        print('체력 {}, 공격력 {}\n'.format(hp, damage))

marine1 = Unit('marine', 40, 5)
marine2 = Unit('marine', 40, 5)
tank = Unit('tank', 150, 35)

# # 불가
# marine3 = Unit('마린')
# marine3 = Unit('마린', 40)

# <멤버 변수>

wraith1 = Unit('레이스', 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))

wraith2 = Unit('빼앗은 레이스', 80, 5)
wraith2.clocking = True

if wraith2.clocking ==True:
    print('{0}는 현재 클로킹 상태입니다.'.format(wraith2.name))

