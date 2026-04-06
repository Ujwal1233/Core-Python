def createarr():
    l=[]
    while True:
        try:
            a=int(input())
            l.append(a)
        except Exception as e:
            return l
print("enter for arr1")         
arr1=createarr()
print("enter for arr2")
arr2=createarr()
def merge_alt(arr1,arr2):
    k=[]
    i,j=0,0
    a1=len(arr1)
    a2=len(arr2)
    while len(k)<(a1+a2):
        if i<a1 :
            k.append(arr1[i])
            i+=1
        if j<a2:
            k.append(arr2[j])
            j+=1
    return k
res=merge_alt(arr1,arr2)
print(arr1)
print(arr2)
print(res)