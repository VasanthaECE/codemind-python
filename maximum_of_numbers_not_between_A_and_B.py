n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
s=max(l)
if x<=s<=y:
    print("-1")
else:
    print(s)