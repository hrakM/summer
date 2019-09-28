s=input()
q=int(input())
r=[input().split() for i in range(q)]
for j in r:
    a,b=int(j[1]),int(j[2])+1
    if j[0]=="replace":
        p=j[3]
        s=s[:a]+p+s[b:]
    elif(j[0]=="reverse"):
        s=s[:a]+s[a:b][::-1]+s[b:]
    elif(j[0]=="print"):
        print(s[a:b])
