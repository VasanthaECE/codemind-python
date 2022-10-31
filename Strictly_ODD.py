n=int(input())
d=list(map(int,input().split()))
c=0
for i in range (n):
    if d[i]%2!=0:
        if i%2!=0:
            c=2
        else:
            c=3
            break
if c==2:
    print("True")
else:
    print("False")
        