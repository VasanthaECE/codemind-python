n,m,l=map(int,input().split())
s=(l+m+n)/2
area=(s*(s-l)*(s-m)*(s-n))**0.5
print(format(area,".2f"))