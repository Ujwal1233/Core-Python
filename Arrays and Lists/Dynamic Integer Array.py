def CreateInt():
    print("Enter the elements into the array to be create")
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=CreateInt()
print("Original Arr:",arr)