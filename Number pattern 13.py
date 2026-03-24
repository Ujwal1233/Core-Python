n = int(input("Enter the number: "))
for i in range(1,(n+1)):
    for j in range(i,(n+i)):
         print(j, end=" ")
    print()