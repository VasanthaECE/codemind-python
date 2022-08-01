n=int(input())
s=0
while (n):
    r=n%10
    s=s+(r*r)
    n=n//10
    if (n==0):
        n=s
        s=0
        if (n>=1) and (n<=9):
            break
if (n==1):
    print("True")
else:
    print("False")
