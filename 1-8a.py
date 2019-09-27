a= input()
lc=a.lower()
uc=a.upper()
d=""
for i in range(len(a)):
    if a[i]==lc[i]:
        d+=uc[i]
    else:
        d+=lc[i]
print(d)
