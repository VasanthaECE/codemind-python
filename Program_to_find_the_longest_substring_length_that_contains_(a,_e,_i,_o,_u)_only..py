n=input()
c=0
s=0
v='aeiou'
for i in n:
    if i in v:
        f=True
    else:
        f=False
    if f==True:
        c+=1
    else:
        c=0
    if c>s:
        s=c
print(s)
        