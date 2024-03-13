#표준 입출력
'''
import sys
print('Python', 'Java',file=sys.stdout)
print('Python', 'Java',file=sys.stderr)

#print('Python', 'Java', 'JavaScript', sep=',', end='?')
#print('무엇이 더 재밌을까요?')

s={'수학':0, '영어':50, '코딩':100}
for su,s in s.items():
    print(su.ljust(8),str(s).rjust(4),sep=':')

#은행 대기순번표
#001,002,003,....
for  n in range(1,21):
    print('대기번호:'+str(n).zfill(3))
'''
#표준 입력
'''
a=input('아무 값이나 입력하세요:')
print(type(a))
print('입력하신 값은 ' + a + '입니다.')
a,b=map(int,input())
print(a,b)
c=list(input().split())
print(c)
'''

#다양한 출력 포맷

print('{0: >10}'.format(500))

print('{0: >+10}'.format(500))
print('{0: >+10}'.format(-500))

print('{0:_<+10}'.format(500))

print('{0:,}'.format(100000000000))

print('{0:+,}'.format(100000000000))

print('{0:^<+30,}'.format(100000000000))
#소수점 출력
print('{0:f}'.format(5/3))

print('{0:.2f}'.format(5/3))



#파일 입출력
'''
#w=쓰기
s=open('score.txt','w',encoding='utf8')
print('수학:0',file=s)
print('영어:50',file=s)
s.close()

#a=추가하기
s=open('score.txt','a',encoding='utf8')
s.write('과학:80')
s.write('\n코딩:100')
s.close()

#r=읽기
s=open('score.txt','r',encoding='utf8')
print(s.read())
s.close()

s=open('score.txt','r',encoding='utf8')
print(s.readline(),end='') #줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(s.readline(),end='')
print(s.readline(),end='')
print(s.readline())
s.close()

s=open('score.txt','r',encoding='utf8')
while True:
    line=s.readline()
    if not line:
        break
    print(line,end='')
s.close()

s=open('score.txt','r',encoding='utf8')
l=s.readlines() #list 형태로 저장
for i in l:
    print(i,end='')
s.close()
'''


#pickle
'''
import pickle

p_f=open('p.pickle', 'wb')
p={'이름':'박명수','나이':30,'취미':['축구','골프','코딩']}
print(p)
pickle.dump(p,p_f) #p에 있는 정보를 p_f에 저장
p_f.close()

p_f=open('p.pickle', 'rb')
p=pickle.load(p_f) #file에 있는 정보를 profile에 불러오기
print(p)
p_f.close()
'''

#with
'''
import pickle

with open('p.pickle','rb') as p_f:
    print(pickle.load(p_f))

with open('study.txt','w',encoding='utf8') as study_f:
    study_f.write('파이썬을 열심히 공부하고 있어요.')

with open('study.txt','r',encoding='utf8') as study_f:
    print(study_f.read())
'''