def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num:"))
            l1.append(n)
        except:
            return l1
def mergesortmerging(arr,start,mid,end):
    i,j=start,(mid+1)
    res=[]
    for k in range(0,((mid+end)+1)):
        if i<=mid and j<=end:
            if arr[i]<=arr[j]:
                res.append(arr[j])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        else:
            if i<=mid:
                res.append(arr[i])
                i+=1
            elif j<=end:
                res.append(arr[j])
                j+=1
        #update the original array
    for k in range(0,len(res)):
        arr[start]=res[k]
        start+=1
def mergesortdivision(arr,start,end):
    if start>=end:
        return
    mid=(start+end)//2
    #LHS division
    mergesortdivision(arr,start,mid)
    #RHS division
    mergesortdivision(arr,(mid+1),end)
    #start merging-After base cond the merging works
    mergesortmerging(arr,start,mid,end)
arr=Intarr()
print("Original Array:",arr)
mergesortdivision(arr,0,(len(arr)-1))
print("Asc Sorted Arr:",arr)