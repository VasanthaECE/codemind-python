n=int(input())
id=0
while n>0:
    r=n%10
    if id<r:
        id=r
    n=int(n/10)
print(id)