str="abcdefghijklmnopqrstuvwxyz"
x=[0]*26
while True:
    try:
        a=input()
    except:
        break
    for A in a:
        index=0
        for B in str:
            if A == B or A == B.upper():
                x[index] += 1
                break
            index += 1
    for i in range(len(str)):
        print("%s : %d"%(str[i],x[i]))
