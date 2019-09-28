n=int(input())
a,b=0,0
for i in range(n):
    c,d=input().split()
    if(c<d):
        b+=3
    elif c==d:
        a+=1
        b+=1
    else:
        a+=3
print(a,b)
