a,b=map(int,input().split())
big=max(a,b)
while True:
    if big%a==0 and big%b==0:
        print(big)
        break
    big+=1