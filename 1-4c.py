for i in range(6):
    a,op,b=input().split()
    a=int(a)
    b=int(b)
    if(op=='?'):
        break
    if(op=='+'):
        print(a+b)
    if(op=='-'):
        print(a-b)
    if(op=='*'):
        print(a*b)
    if(op=='/'):
        print(a//b)
