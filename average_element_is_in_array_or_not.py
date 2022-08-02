n=int(input())
d=list(map(int,input().split()))
s=sum(d)
c=s//n
if c in d:
    print("True")
else:
    print("False")