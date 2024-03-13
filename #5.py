#리스트 (list)
'''
a1=10
a2=20
a3=30

a=[10,20,30]
print(a)

a=['유재석','조세호','박명수']
print(a)

print(a.index('조세호'))

a.append('하하')
print(a)

a.insert(1,'정형돈')
print(a)

print(a.pop())
print(a)

a.append('유재석')
print(a)
print(a.count('유재석'))

a=[1,2,3,7,4]
a.sort()
print(a)

a.reverse()
print(a)

a.clear()
print(a)

a=[1,2,3,7,4]
b=['pineapple',20,True]
print(b)

a.extend(b)
print(a)
'''


#사전 (dict)
'''
a={3:'강동수',100:'김유찬'}
print(a[3])
print(a.get(100))

#print(a[5])
print(a.get(5))
print(a.get(5,'사용 가능'))
      #bool
print(3 in a) 
print(5 in a)

a={'A-3':'강동수','b-100':'김유찬'}
print(a['A-3'])
print(a['b-100'])

#새 손님
print(a)
a['A-3']='류동하'
a['C-20']='박교연'
print(a)

#간 손님
del a['A-3']
print(a)

print(a.keys())
print(a.values())
print(a.items())
print(a.clear())
a.clear()
print(a)
'''


#튜플 (tuple)
'''
a=("돈까스",'치즈까스')
print(a[0])
print(a[1])

#값 추가 or 변경 불가

name='김종국'
age=20
hobby='코딩'
print(name,age,hobby)

name,age,hobby='김종국',20,'코딩'
print(name,age,hobby)
'''


#집합 (set)
#중복 안됨, 순서 없음
'''
a={1,3,5,2,2,4,4}
print(a)

java={'유재석','김태호','양세형'}
python=set(['유재석','박명수'])

    #교집합
print(java&python)
print(java.intersection(python))

    #합집합
print(java | python)
print(java.union(python))

    #차집합
print(java-python)
print(java.difference(python))

python.add('김태호')
print(python)

java.remove('김태호')
print(java)
'''


#자료구조의 변경
'''
a={'커피','주스','우유'}
print(a,type(a))

a=list(a)
print(a,type(a))

a=tuple(a)
print(a,type(a))

a=set(a)
print(a,type(a))
'''



















