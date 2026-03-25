n = int(input("Enter the value:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print(chr(96+n), end=" ")
        else:
            print(" ", end=" ")
    print()