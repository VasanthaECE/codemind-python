def fib(n):
    a,b=0,1
    if n==1:
        print(a)
    else:
        print(a,b,end=" ")
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
n=int(input())
fib(n)