n=int(input())
e=0
o=0
c=0
while n!=0:
    c+=1
    r=n%10
    n=n//10
    if r%2==0:
        e+=1
    else:
        o+=1
if e==c:
    print("Even")
elif o==c:
    print("Odd")
else:
    print("Mixed")