n=int(input())
l=list(map(int,input().split()))
s=0
l=l+l
for i in range(n):
    if(l[i]%2 and l[i+2]%2==0) or (l[i]%2==0 and l[i+2]%2):
        s+=1
print(s)