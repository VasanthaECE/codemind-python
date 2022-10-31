n=int(input())
l=list(map(int,input().split()))[:n]
s=0
c=0
for i in range(len(l)):
    s=s+l[i]
avg=s//n
for j in range(len(l)):
    if l[j]<=avg:
        c+=1
print(c)