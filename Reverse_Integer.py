def rev(n):
    s=0
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
if n<0:
    n=abs(n)
    p=rev(n)
    print("-",end="")
    print(p)
else:
    p=rev(n)
    print(p)