n=input()
a=input().split()
j=int(n)-1

for i in range(int(n)):
    print(str(a[j])+" ", end="")
    j=j-1
