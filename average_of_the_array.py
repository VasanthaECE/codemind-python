n=int(input())
d=list(map(int,input().split()))
s=sum(d)
c=s/n
res = "{:.2f}".format(c)
print(res)