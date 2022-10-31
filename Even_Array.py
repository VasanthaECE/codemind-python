n=int(input())
d=list(map(int,input().split()))
c=0
for i in range (n):
    if d[i]%2!=0:
        c=2
        break
if c==2:
    print("False")
else:
    print("True")

