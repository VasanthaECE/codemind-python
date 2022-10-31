n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
f,g=min(a,b),max(a,b)
c=0
for i in d:
    if i<f or i>g:
        c=c+i
print(c)
        
    