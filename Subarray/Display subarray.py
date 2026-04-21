def createIntarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num"))
            l1.append(n)
        except:
            return l1
        
def displaySubarray(arr):
    for i in range(0,(len(arr))):
        res=[]
        for j in range(i,len(arr)):
            res.append(arr[j])
            print(res)
arr=createIntarr()
print("The original array",arr)
displaySubarray(arr)


def CreateSubarrays(arr):
    res=[]
    for i in range(0,len(arr)):
        sub=[]
        for k in range(i,j+1):
            sub.append(arr[k])
        res.append(sub)
    return res
arr=createIntarr()
print("The original array",arr)
displaySubarray(arr)