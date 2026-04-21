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
