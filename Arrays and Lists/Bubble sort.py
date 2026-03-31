def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except:
            return l1
def Bubblesort(arr):
    n=len(arr)
    for i in range(0,(n-1)):
        for j in range(0,(n-1-i)):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=Intarr()
print("Original arr:",arr)
res=Bubblesort(arr)
print(f"The Sorted array is:{res}")