from math import sqrt
def aut(n):
    s=n*n
    if s<99:
        d=s%10
    if s>999:
        d=s%100
    if s>9999:
        d=s%1000
    if n==d:
        print("Automorphic Number")
    else:
        print("Not an Automorphic Number")
n=int(input())
v=aut(n)