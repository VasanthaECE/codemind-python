n=int(input())
d=list(map(int,input().split()))
s=sum(d)
if s%2==0:
    print("1")
else:
    print("0")