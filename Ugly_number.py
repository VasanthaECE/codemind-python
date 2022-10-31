n=int(input())  #8
s=0
while n!=1:   #8!=0
    if n%5==0:
        n=n//5
    elif n%3==0:
        n=n//3
    elif n%2==0:
        n=n//2
    else:
        s=1
        print("Not Ugly Number")
        break
if s==0:
    print("Ugly Number")