#cording: utf-8
for i in range(3):

    print('数字を入力してください入力例:a b')
    a,b=input().split()
    print ('aの値',a)
    print ('bの値',b)

    if(int(a)>int(b)):
        print ('a>b')
    elif(int(b)>int(a)):
        print ('a<b')
    elif(int(a)==int(b)):
        print ('a=b')
