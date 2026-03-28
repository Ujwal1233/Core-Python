def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except:
            return l1
def findMaxEle(arr):
    maxele,maxeleindex=-2**32,-1
    for i in range(0,len(arr)):
        if arr[i]>maxele:
            maxele=arr[i]
            maxeleinddex=i
    return maxele,maxeleindex
arr=Intarr()
print("Original Arr:",arr)
resMaxele,resMaxeleindex=findMaxEle(arr)
print(f"The max ele in arr is:{resMaxele} at index:{resMaxeleindex}")
        
