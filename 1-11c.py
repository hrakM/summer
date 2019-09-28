a,b=[input().split()for i in '12']
b[3:5]=b[4],b[3]
c=0
for j in ("012345","152304","215043","310542","402351","513240"):
    e=[a[int(k)]for k in j]
    e[3:5]=e[4:2:-1]
    if(e[0]==b[0]):
        e=e[1:5]*2
        for l in range(4):
            if e[l:l+4]==b[1:5]:c=1
print(("No","Yes")[c])
