n=int(input())
ev=0
od=0
d=list(map(int,input().split()))
for i in range(n):
    if i%2==0:
        ev=ev+d[i]
    if i%2!=0:
        od=od+d[i]
print(abs(ev-od))