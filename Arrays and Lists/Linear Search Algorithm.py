def LinearSearch():
    print("Enter the values into the array to be create")
    l1=[]
    while True:
        try:
            n=int(input("Enter a value:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=LinearSearch()
target=int(input("Enter a num:"))
flag,index=False,-1
for i in range(0,len(arr)):
    if target==arr[i]:
        flag=True
        index=i
        break
print("Original Arr:",arr)
if flag:
    print(f"The {target} is found at index:{index}")
else:
    print(f"{target} not found")

