a=[]
i=0
while(True):
    print("Enter a value")
    num=int(input())
    a.insert(i,num)
    i+=1
    print("Do you want to continue")
    print("1. Yes")
    print("2. No")  
    choice=int(input())
    if(choice==1):
        continue
    else:
        break
print(a)