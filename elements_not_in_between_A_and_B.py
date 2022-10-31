n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=1
for i in l:
    if i<a or i>b:
        d=2
        print(i,end=" ")
if d==1:
    print(-1)