n=(input())
s=int(n[:2])
m=int(n[3:])
a=abs(30*s-5.5*m)
if a>180:
    a=360-a
print(a)