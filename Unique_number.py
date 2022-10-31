n=int(input())
d=list()
f=0
while n>0:
    r=n%10
    d.append(r)
    n=n//10
for i in d:
    if d.count(i)>1:
        f=1
        break
if f==1:
    print("Not Unique Number")
else:
    print("Unique Number")