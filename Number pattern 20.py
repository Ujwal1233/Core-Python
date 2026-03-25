n=int(input("Enter a num:"))
count=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2!=0:
            print(count,end=" ")
            countdecre=count
        else:
            print(countdecre,end=" ")
            countdecre-=1
        count+=1
    print()
    countdecre+=n