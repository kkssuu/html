N=int(input())
l=[0]
for i in range(N):
    M=int(input())
    l.append(M)



res=[]

visit=[False]*(N+1)
def f(n):
    l1=[]
    if visit[n]==True:
        res.append(n)
        return
    visit[n]=True
    l1.append(n)
    q=l[n]
    f(q)

for j in range(1,N+1):
    f(j)

print(res)
'''
res=set(res)
print(len(res))
for k in res:
    print(k)
'''