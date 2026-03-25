n=int(input("Enter a value:"))
noc=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if noc%2!=0:
            print(chr(64+noc),end=" ")
        else:
            print(chr(96+noc),end=" ")
        noc+=1
    print()