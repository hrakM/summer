while True:
    h,w=map(int,input().split())
    if h+w==0:
        break


    for i in range(0,h):
        frame=""
        for j in range(0,w):
            if i==0 or i==h-1 or j==0 or j==w-1:
                frame += "#"
            else:
                frame += "."
        print(frame)
