n = int(input("Enter the number: "))
noc=1
for i in range(1,(n*2)):
    for j in range(noc,(n+1)):
         print(j, end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1