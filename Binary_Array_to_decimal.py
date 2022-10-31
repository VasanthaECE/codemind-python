n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(len(l)):
    a=a+(l[i]*(2**n))
    n-=1
print(a//2)