#숫자 처리 함수
'''
print(abs(-5))
print(pow(4,3))
print(max(5,12))
print(min(5,12))
print(round(5.3))

from math import*
print(floor(4.3))
print(ceil(3.14))
print(sqrt(16))
'''


#랜덤 함수
'''
from random import*
#import random
#random.randint()
print(random())         #0.0<=x<1.0
print(random()*10)      #0.0<=x<10
print(int(random()*10))
print(int(random()*10)+1)

print(int(random()*45)+1) #로또 번호

print(randrange(1,46))
print(randint(1,45))
'''


#퀴즈 2
'''
from random import*
x=randint(4,28)
print('오프라인 스터디 모임 날짜는 매월 '+ str(x) +'일로 설정되었습니다.')
'''


#문자열 처리 함수

x="Python is Amazing"
print(x.lower())
print(x.upper())
print(x[0].isupper())
print(x[0].islower())
print(len(x))
print(x.replace('Python','Java'))

y=x.index('n')
print(y)
y=x.index('n',y+1)
print(y)

print(x.find('Java'))
#print(x.index('Java'))

print(x.count('n'))



#문자열 포맷
'''
print('a'+'b')
print('a','b')

#방법 1
print('나는 %d살입니다.'%20)
print('나는 %s을 좋아해요.'%'파이썬')
print('Apple은 %c로 시작해요.'%'A')

print('나는 %s살입니다.'%20)
print('나는 %s색과 %s색을 좋아해요.'%('파란','빨간'))

#방법 2
print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란','빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란','빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란','빨간'))

#방법 3
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age=20,color='빨간'))

#방법 4 (v3.6 이상~)
age=20
color='빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')
'''


#탈출 문자
'''
#\n:줄바꿈
print("백문이 불여일견\n백견이 불여일타")

print("저는 \"나도코딩\"입니다.")

print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")

#\r:커서를 맨 앞으로 이동
print("Red Apple\rPine")
#PineApple

#\b:백스페이스
print("Redd\bApple")
#RedApple

#\t:탭
print("Red\tApple")
'''


#퀴즈 3
'''
x=input()
y=x.index('/')
y=x[x.index('/',y+1)+1:]
z=y[:y.index('.')]
p=z[0:3]+str(len(z))+str(z.count('e'))+'!'
print("{1}의 비밀번호는 {0}입니다.".format(p,x))
'''










