x=0
n=int(input())
a=list(map(int,input().split()))
for i in range(int(n-1)):
    b=list(map(int,input().split()))
    if a[0]==b[1]:
        b[0],b[1],b[4],b[5]=b[1],b[5],b[0],b[4]
    elif a[0]==b[2]:
        b[0],b[2],b[3],b[5]=b[2],b[5],b[0],b[3]
    elif a[0]==b[3]:
        b[0],b[2],b[3],b[5]=b[3],b[0],b[5],b[2]
    elif a[0]==b[4]:
        b[0],b[1],b[4],b[5]=b[4],b[0],b[5],b[1]
    elif a[0]==b[5]:
        b[0],b[1],b[4],b[5]=b[5],b[4],b[1],b[0]
    for j in range(4):
        if a[1]==b[1]:
            break
        a[1],a[3],a[4],a[2]=a[3],a[4],a[2],a[1]
    if a==b:
        x=x+1
if x==0:
    print('yes')
else:
    print('no')
