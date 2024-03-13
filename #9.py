
'''
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name='마린'
hp=40
damage=5

print('{0} 유닛이 생성되었습니다.'.format(name))
print('체력 {0}, 공격력 {1}\n'.format(hp,damage))

#탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드/시즈 모드.
t_n='탱크'
t_h=150
t_d=35

print('{0} 유닛이 생성되었습니다.'.format(t_n))
print('체력 {0}, 공격력 {1}\n'.format(t_h,t_d))

t2_n='탱크'
t2_h=150
t2_d=35

print('{0} 유닛이 생성되었습니다.'.format(t2_n))
print('체력 {0}, 공격력 {1}\n'.format(t2_h,t2_d))

def a(name, location, damage):
    print('{0}:{1}방향으로 적군을 공격합니다. [공격력:{2}]'.format(\
        name,location,damage))
    
a(name,'1시',damage)
a(t_n,'1시',t_d)
a(t2_n,'1시',t2_d)
'''

#클래스
#__init__함수는 생성자 
# 마린,탱크는 Unit클래스의 인스턴스
#지금 이 Unit클래스에선 n(name),h(hp),d(damage)가 '멤버변수'라는 것이다
'''
class Unit:
    def __init__(s,n,h,d):
        s.n=n
        s.h=h
        s.d=d
        print('{0} 유닛이 생성되었습니다.'.format(s.n))
        print('체력 {0}, 공격력 {1}'.format(s.h,s.d))

#m1=Unit('마린',40,5)
#m2=Unit('마린',40,5)
#t=Unit('탱크',150,35)

#레이스 : 공중 유닛, 비행기. 클로킹 (은신)
w1=Unit('레이스',80,5)
print('유닛 이름: {0}, 공격력: {1}'.format(w1.n,w1.d))

#마인드 컨트롤: 상대방 유닛을 내 유닛으로 만듬
w2=Unit('빼앗은 레이스',80,5)
w2.c=True

if w2.c==True:
    print('{0}는 현재 클로킹 상태입니다.'.format(w2.n))
'''
from random import*
#일반 유닛
class Unit:
    def __init__(s,n,h,sp):
        s.n=n
        s.h=h
        s.sp=sp
        print('{0} 유닛이 생성되었습니다.'.format(n))

    def mv(s,l):
        #print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로  이동합니다. [속도 {2}]'\
              .format(s.n,l,s.sp))

    def da(s,d):
        print('{0} : {1}데미지를 입었습니다.'.format(s.n,d))
        s.h-=d
        print('{0} : 현재체력은 {1}입니다.'.format(s.n,s.h))
        if s.h<=0:
            print('{0} : 파괴되었습니다.'.format(s.n))

#공격 유닛
class AttackUnit(Unit):     #상속
    def __init__(s,n,h,sp,d):
        Unit.__init__(s,n,h,sp)
        s.d=d
        
    def a(s,l):             #메소드
        print('{0} : {1}방향으로 적군을 공격합니다.[공격력 {2}]'\
              .format(s.n,l,s.d))
#마린
class Marine(AttackUnit):
    def __init__(s):
        AttackUnit.__init__(s,'마린',40,1,5)

    # 스팀팩: 일정시간 동안 이동 및 공격속도 증가, 체력 10감소
    def stimpack(s):
        if s.h>10:
            s.h-=10
            print('{0} : 스팀팩을 사용합니다. (HP 10 감소)'.format(s.n))
        else:
            print('{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.'.format(s.n))

#탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 공격력으로 공격한다. 이동 불가.
    seize=False

    def __init__(s):
        AttackUnit.__init__(s,'탱크',150,1,35)
        s.seize_m=False

    def set_seize_m(s):
        if Tank.seize==False:
            return 
        
        #현재 시즈모드가 아닐 때 -> 시즈모드
        if s.seize_m==False:
            print('{0} : 시즈모드로 전환합니다.'.format(s.n))
            s.d *= 2
            s.seize_m=True
        #현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print('{0} : 시즈모드를 해제합니다.'.format(s.n))
            s.d /=2
            s.seize_m=False 


'''
#메딕:의무병

#파이어뱃 : 공격 유닛, 화염방사기.
f1=AttackUnit('파이어뱃',50,16)
f1.a('5시')

#공격 2번 받는다고 가정
f1.da(25)
f1.da(25)
'''
#드랍쉽:공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송.공격 X
class Flyable:
    def __init__(s,f_s):
        s.f_s=f_s

    def fly(s,n,l):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'\
              .format(n,l,s.f_s))
    
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):        #다중상속
    def __init__(s,n,h,d,f_s):
        AttackUnit.__init__(s,n,h,0,d) #지상 speed 0
        Flyable.__init__(s,f_s)

    def mv(s,l):                                    #메소드 오버라이딩
        #print('[공중 유닛 이동]')
        s.fly(s.n,l)

#레이스 
class Wraith(FlyableAttackUnit):
    def __init__(s):
        FlyableAttackUnit.__init__(s,'레이스',80,20,5)
        s.clocked=False #클로킹 모드 (해제 상태)
        
    def clocking(s):
        if s.clocked==True:             #클로킹 모드 ->모드 해제
            print('{0} : 클로킹 모드 해제합니다.'.format(s.n))
            s.clocked=False
        else:                           #클로킹 모드 해제 ->모드 설정
            print('{0} : 클로킹 모드 설정합니다.'.format(s.n))
            s.clocked=True


'''
#발키리:공중 공격 유닛, 한번에 14발 미사일 발사.
v=FlyableAttackUnit('발키리',200,6,5)
v.fly(v.n,'3시')


#벌쳐:지상 유닛, 기동성이 좋음
vult=AttackUnit('벌쳐',80,10,20)

#배틀크루저: 공중 유닛, 체력 많음, 공격력도 좋음
bc=FlyableAttackUnit('배틀크루저',500,25,3)

vult.mv('11시')
#bc.fly(bc.n,'9시')
bc.mv('9시')


# 건물
class BuildingUnit(Unit):
    def __init__(s,n,h,l):
        #Unit.__init__(s,n,h,0)
        super().__init__(n,h,0)                 #super
        s.l=l

class Unit:
    def __init__(s):
        print('Unit 생성자')
    
class Flyable:
    def __init__(s):
        print('Flyable 생성자')

class FlyableUnit(Flyable,Unit):
    def __init__(s):
        #super().__init__()                 #처음 것만 호출
        Unit.__init__(s)
        Flyable.__init__(s)
#드랍쉽
d=FlyableUnit()

# 서플라이 디폿: 건물, 1개 건물 = 8 유닛 생성. 
sup=BuildingUnit('서플라이 디폿', 500, '7시')
'''
def g_s():
    print('[알림] 새로운 게임을 시작합니다.')

def g_o():
    #pass                                    #pass #일단 완성된 것처럼 넘어감
    print('Player:gg') #goodgame
    print('[Player] 님이 게임에서 퇴장하셨습니다.')

#게임 시작
g_s()

#마린 3기 생성
m1=Marine()
m2=Marine()
m3=Marine()

#탱크 2기 생성
t1=Tank()
t2=Tank()

#레이스 1기 생성
w1=Wraith()

#유닛 일괄 관리
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.mv('1시')

#탱크 시즈모드 개발
Tank.seize=True
print('[알림] 탱크 시즈 모드 개발이 완료되었습니다.')


# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_m()
    elif isinstance(unit,Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.a('1시')

#전군 피해
for unit in attack_units:
    unit.da(randint(5,21)) #공격은 랜덤으로 받음 (5~20)

#게임 종료
g_o()



