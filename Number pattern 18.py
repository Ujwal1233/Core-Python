n=int(input("Enter a num:"))
for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if i<j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()