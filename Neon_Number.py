n=int(input())
s=0
p=n*n
while p:
    r=p%10
    s=s+r
    p=p//10
if n==s:
    print("Neon Number")
else:           
    print("Not Neon Number")