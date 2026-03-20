n=int(input("enter no : "))
x=n
for i in range(1,n*2):
    for j in range(1,x+1):
        print("*",end="")
    print()
    if i<n:
        x-=1
    else:
        x+=1