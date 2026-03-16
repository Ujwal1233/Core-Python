n=int(input("Enter a num:"))
for i in range(n,(1-1),-1):
    for k in range(n,i,-1):
         print(" ",end=" ")
    for j in range(1,(i+1)):
        print("*",end=" ")
    print()