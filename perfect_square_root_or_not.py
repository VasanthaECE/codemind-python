from math import sqrt
def per(n):
    s=int(sqrt(n))
    r=s**2
    if n==r:
        print("True")
    else:
        print("False")
n=int(input())
c=per(n)