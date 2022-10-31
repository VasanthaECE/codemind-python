a,b,s=map(int,input().split())
c=0
for i in range(a,b+1):
    if i%s==0:
        c+=1
print(c)