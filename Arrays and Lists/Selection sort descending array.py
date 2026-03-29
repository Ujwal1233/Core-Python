def Intarr():
    l1=[]
    while True:
        try:
            n=(int(input("Enter the num:")))
            l1.append(n)
        except:
            return l1
def Intarr():
    l1 = []
    while True:
        try:
            n = int(input("Enter a num: "))
            l1.append(n)
        except:
            return l1

def DescendingArr(arr):
    n = len(arr)

    # Cycles
    for i in range(0, (n - 1)):
        actualInd = ((n - 1) - i)

        # Current cycle's minimum element
        currminele, currmineleind = 2**32, -1

        for j in range(0, (n - i)):
            if arr[j] < currminele:
                currminele = arr[j]
                currmineleind = j

        # Swap
        arr[actualInd], arr[currmineleind] = arr[currmineleind], arr[actualInd]


arr = Intarr()
print("Original Arr:", arr)

DescendingArr(arr)

print(f"The descending sorted array is: {arr}")