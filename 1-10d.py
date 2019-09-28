import math
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))
z=[abs(x[i]-y[i])for i in range(n)]
for j in range(1,4):
    a=0
    for k in z:
        a+=k**j
    print("{:.6f}".format(a**(1/j)))
print("{:.6f}".format(max(z)))
