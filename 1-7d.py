n,m,l=map(int,input().split())
x=[]
y=[]
for i in range(n):
    x.append(list(map(int,input().split())))
for j in range(m):
    y.append(list(map(int,input().split())))
for i in range(n):
    z=[]
for j in range(l):
    a=0
    for k in range(m):
        a+=x[i][k]*y[k][j]
    z.append(a)
print(" ".join(list(map(str,z))))
