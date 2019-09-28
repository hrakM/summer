class dice():
    def __init__(s,n):
        s.n=n
    def move(s,c):
        if c=='E':
            s.n=[s.n[i] for i in [3,1,0,5,4,2]]
        if c=='S':
            s.n=[s.n[i] for i in [4,0,2,3,5,1]]
        if c=='N':
            s.n=[s.n[i] for i in [1,5,2,3,0,4]]
        if c=='W':
            s.n=[s.n[i] for i in [2,1,5,0,4,3]]
n=[int(x) for x in input().split()]
c= input()
d = dice(n)
for j in c:
    d.move(j)
print(d.n[0])
