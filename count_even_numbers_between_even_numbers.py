n=int(input())
d=list(map(int,input().split()))
c=0
for i in range(n-2):
    if d[i]%2==0 and d[i+2]%2==0:
        if d[i+1]%2==0:
            c=c+1
print(c)
            