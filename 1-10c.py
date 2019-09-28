import math
while True:
    n=int(input())
    if n==0:
        break
    m=list(map(int,input().split()))
    a=sum(m)/n
    v=0
    for i in m:
        v+=(i-a)**2
    r=(v/n)**0.5
    print("{:.8f}".format(r))
