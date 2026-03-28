def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except:
            return l1
def findMinEle(arr):
    minele,mineleindex=2**32,-1
    for i in range(0,len(arr)):
        if arr[i]<minele:
            minele=arr[i]
            mineleinddex=i
    return minele,mineleindex
arr=Intarr()
print("Original Arr:",arr)
resMinele,resMineleindex=findMinEle(arr)
print(f"The min ele in arr is:{resMinele} at index:{resMineleindex}")
        