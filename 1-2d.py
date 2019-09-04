#cording: utf-8
for i in range(2):

    print('W,H,x,y,rを入力してください')
    w,h,x,y,r=input().split()
    print("input: "+str(w)+' '+str(h)+' '+str(x)+' '+str(y)+' '+str(r)+' ')
    wh=int(w)*int(h)
    pi=3.14
    rpi=int(r)^2*int(pi)
    print('wh:',wh)
    print('r^2*pi:',rpi)

    if(int(w)<int(x)+int(r) or int(h)<int(y)+int(r) or 0>int(x)-int(r) or 0>int(y)-int(r)):
        print('Output: No')
    else:
        print('Output: Yes')
