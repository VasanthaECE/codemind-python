a,b=map(int,input().split())
while(b!=0):
    a,b=b,a
    b=b%a
gcd=a
print(gcd)