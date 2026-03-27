def CreateStr():
    print("Enter the values into the array to be create")
    l1=[]
    while True:
        n=input("Enter a value:")
        if n=="":
            return l1
        l1.append(n[:1])
arr=CreateStr()
print("Original Arr:",arr)