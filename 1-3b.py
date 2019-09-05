print('0を入力すると終了します。')
print('任意の数値を入力してください。: ')
n=1
m=0
l= list(iter(input,'0'))
for i in l:
    print('Case'+str(n)+':'+str(l[m]))
    n=n+1
    m=m+1
