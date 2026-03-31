def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num"))
            l1.append(n)
        except:
            return l1
def Seclarele(arr):
    maxele,maxeleind=-2**32,-1
    secmaxele,secmaxeleind=-2**32,-1
    for i in range(0,len(arr)):
        if maxele<arr[i]:
            secmaxele=maxele
            secmaxeleind=maxeleind
            maxele=arr[i]
            maxeleind=i
        elif maxele!=arr[i] and secmaxele<arr[i]:
            secmaxele=arr[i]
            secmaxeleind=i
    return [maxele,maxeleind,secmaxele,secmaxeleind]
arr=Intarr()
print("Original Arr:",arr)
res=Seclarele(arr)
print(f"The max element of an array is:{res[0]} at index:{res[1]}")
print(f"Second max ele",res[2],"at index:",res[3])
            