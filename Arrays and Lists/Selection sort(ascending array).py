def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except:
            return l1
def AscendingArr(arr):
    n=len(arr)
    #Cycles
    for i in range(0,(n-1)):
        actualInd=((n-1)-i)
        #Current cycles max ele ind
        currmaxele,currmaxeleind=-2**-32,-1
        for j in range(0,(n-i)):
            if arr[j]>currmaxele:
                currmaxele=arr[j]
                currmaxeleind=j
        arr[actualInd],arr[currmaxeleind]=arr[currmaxeleind],arr[actualInd]
arr=Intarr()
print("Original Arr:",arr)
AscendingArr(arr)
print(f"The ascending sorted array is:{arr}")