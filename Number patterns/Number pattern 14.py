n = int(input("Enter the number: "))
for i in range(n,1-1,-1):
    for j in range(i,i+n):
         print(j, end=" ")
    print()