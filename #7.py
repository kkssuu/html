#함수
'''
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()
'''


#전달값과 반환값
'''
def deposit(balance,money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance,money):
    if balance>=money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance,money):
    commission=100 #수수료 100원
    return commission, balance-money-commission

balance=0
balance=deposit(balance,1000)
balance=withdraw(balance,2000)
balance=withdraw(balance,500)
commission, balance=withdraw_night(balance,500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission,balance))
'''

#기본값
'''
def profile(name,age,main_lang):
    print("이름:{0}\t나이:{1}\t주 사용 언어:{2}"\
          .format(name,age,main_lang))
    
profile("유재석",20,"파이썬")
profile("김태호",25,"자바")

def profile(name,age=17,main_lang="파이썬"):
    print("이름:{0}\t나이:{1}\t주 사용 언어:{2}"\
          .format(name,age,main_lang))
    
profile("유재석")
profile("김태호")
'''

#키워드값
'''
def profile(name,age,main_lang):
    print(name,age,main_lang)

profile(name="유재석",main_lang="파이썬",age=20)
profile(main_lang="자바",age=25,name="김태호")
'''

#가변인자
'''
#def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#    print("이름:{0}\t나이:{1}\t".format(name,age),end=' ')
#    print(lang1,lang2,lang3,lang4,lang5)

def profile(name,age,*language):
    print("이름:{0}\t나이:{1}\t".format(name,age),end=' ')
    for lang in language:
        print(lang, end=' ')
    print()

profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
profile("김태호",25,"Kotlin","Swift")
'''


#지역변수와 전역변수
'''
gun=10

def cp(s): 
    global gun
    gun=gun-s
    print("[함수 내]남은 총:{0}".format(gun))

def cp_r(gun,s):
    gun=gun-s
    print("[함수 내] 남은 총:{0}".format(gun))
    return gun

print("전체 총:{0}".format(gun))
#cp(2)
gun=cp_r(gun,2)
print("남은 총:{0}".format(gun))
'''
N=int(input())
visit=[False]*(N+1)
res=[]
l=[0,1,2,3,4]
def f(n):
    if visit[n]==True:
        res.append(n)
        return
    visit[n]=True
    f(l[n])

f(1)
print(set(res))