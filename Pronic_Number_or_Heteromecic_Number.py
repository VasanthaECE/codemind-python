def pro(n):
    for i in range(1,n+1):
        s=i*(i+1)
        if n==s:
            print("YES")
            break
    else:
        print("NO")
n=int(input())
k=pro(n)