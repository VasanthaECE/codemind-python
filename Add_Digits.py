def digSum(n):#38
    if (n%9==0):#38%9==0
        return 9
    else:
        return(n%9)#38%9=2
n=int(input())
print(digSum(n))