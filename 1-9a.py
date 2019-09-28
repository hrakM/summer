w=input().lower()
ans=0
while True:
    t=input()
    if(t=="eot"):
        break
    ans+=t.lower().split().count(w)
print(ans)
