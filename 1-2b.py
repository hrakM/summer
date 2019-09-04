#cording: utf-8
for i in range(2):

    print('3つの値を入力してください.')
    a,b,c=input().split()
    print(str(a)+str(b)+str(c)+'が入力されました.')

    if(int(a)<int(b)<int(c)):
        print('yes')
    else:
        print('no')
