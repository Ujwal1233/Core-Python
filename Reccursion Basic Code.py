def printNum(n):
    if n<=0:
        return
    print(n,end=" ")
    printNum(n-1)
n=int(input("Enter num:"))
printNum(n)