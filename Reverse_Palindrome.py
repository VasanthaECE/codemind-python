n=int(input())
c=n
while n!=0:
    a=str(c)
    b=a[::-1]
    c=c+int(b)
    d=str(c)
    e=d[::-1]
    if d==e:
        print(int(d))
        break