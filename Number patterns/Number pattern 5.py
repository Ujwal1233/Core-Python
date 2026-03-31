n=int(input("Enter a num:"))
for i in range(n,1-1,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()
    