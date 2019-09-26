r,c=map(int,input().split())
a=[]
rr=[]
for i in range(r):
    a.append(list(map(int,input().split())))
    a[i].append(sum(a[i]))
for i in range(r):
    print(" ".join(list(map(str,a[i]))))
cc=[]
for j in range(c+1):
    s=0
    for i in range(r):
        s+=a[i][j]
    cc.append(s)
print(" ".join(list(map(str,cc))))
