n=int(input())
d=list(map(int,input().split()))
s=d[::-1]
for i in range(len(s)):
    if s[i]%2!=0:
        print(s[i])
        break