#cording: utf-8
print('３つの数値を入力してください.')
a,b,c=input().split()
print(str(a)+','+str(b)+','+str(c)+'が入力されました.')

list=[int(a),int(b),int(c)]
d=sorted(list)
print("元のリスト",list)
print("ソート後",d)
print('output: '+str(d[0])+" "+str(d[1])+" "+str(d[2]))
