a = input()
b,c = divmod(a,3600)
d,e = divmod(c,60)
print(str(b)+":"+str(d)+":"+str(e))
