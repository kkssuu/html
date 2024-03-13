#모듈
'''
import theater_module
theater_module.price(3) #3명이서 영화 보러갔을 때 가격
theater_module.price_morning(4) #4명이서 조조할인영화
theater_module.price_soldier(5) #5명의 군인이 영화보러감


import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)


from theater_module import*
#from random import*
price(3)
price_morning(4)
price_soldier(5)


from theater_module import price, price_morning
price(5)
price_morning(6)
#price_soldier(7)


from theater_module import price_soldier as price
price(5)
'''

#패키지 (모듈을 모아놓은 집합)
'''
import travel.thailand
#import travel.thailand.ThailandPackage()
trip_to=travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to=vietnam.VietnamPackage()
trip_to.detail()
'''
#__all__
'''
#from random import *
from travel import* 
#trip_to=vietnam.VietnamPackage()
trip_to=thailand.ThailandPackage()
trip_to.detail()
'''

#패키지, 모듈 위치
'''
from travel import* 
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
'''

#pip install
#pip ??

#내장함수

#input: 사용자 입력을 받는 함수
#l=input()

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 갖고 있는지 표시

print(dir())
import random
print(dir())
import pickle
print(dir())

import random
print(dir(random))

l=[1,2,3]
print(dir(l))

n='Jim'
print(dir(n))


#외장함수
#glob: 경로 내의 폴더/파일 목록 조회 (윈도우 dir)
'''
import glob
print(glob.glob('*.py')) #확장자가 py인 모든 파일


#os : 운영체제에서 제공하는 기본 기능

import os

print(os.getcwd()) #현재 디렉토리

f='sample_dir'

if os.path.exists(f):
    print('이미 존재하는 폴더입니다.')
    os.rmdir(f)
    print(f,'폴더를 삭제하였습니다.')
else:
    os.makedirs(f) #폴더 생성
    print(f,'폴더를 생성하였습니다.')

print(os.listdir())


#time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print('오늘 날짜는',datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today=datetime.date.today()
td=datetime.timedelta(days=100)
print('우리가 만난지 100일은', today+td)
'''



