n=int(input("enter no : "))
x=1
for i in range(1,n*2):
    for k in range(n,x,-1):
        print(" ",end="")
    for j in range(1,x+1):
        print("* ",end="")
    print()
    if i<n:
        x+=1
    else:
        x-=1