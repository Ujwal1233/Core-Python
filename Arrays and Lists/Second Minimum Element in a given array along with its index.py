def Intarr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num"))
            l1.append(n)
        except:
            return l1
def Secminele(arr):
    minele,mineleind=2**32,-1
    secminele,secmineleind=2**32,-1
    for i in range(0,len(arr)):
        if minele>arr[i]:
            secminele=minele
            secmineleind=mineleind
            minele=arr[i]
            mineleind=i
        elif minele!=arr[i] and secminele>arr[i]:
            secminele=arr[i]
            secmineleind=i
    return [minele,mineleind,secminele,secmineleind]
arr=Intarr()
print("Original Arr:",arr)
res=Secminele(arr)
print(f"The min element of an array is:{res[0]} at index:{res[1]}")
print(f"Second min ele",res[2],"at index:",res[3])
            