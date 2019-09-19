a,b=input().split()
if (int(a)>=1 and int(b)<=10**9):
    d=int(a)//int(b)
    r=int(a)%int(b)
    f=float(a)/float(b)
    print(d,"",r,"",'{:.10g}'.format(f))
