def isEVENodd(n):
    return n%2==0
count=int(input("Enter a count of num"))
num=1
print(f"First {count} Even Num's:")
while count>0:
    flag=isEVENodd(num)
    if flag:
        print(num,end=" ")
        count-=1
    num+=1