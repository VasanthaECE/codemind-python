n=int(input())
for i in range(0,n):
    n=int(input())
    s=1
    for i in range(2,n+1):
        s*=i
    print(s)