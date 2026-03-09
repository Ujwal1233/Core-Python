def isEVENODD(n):
    return n%2==0
sr=int(input("Enter a sr num:"))
er=int(input("Enter a er num:"))
if sr>er:
       print("Invalid output.")
else:
       print("Even num:",end=" ")
for i in range(sr,er+1):
    flag=isEVENODD(i)
    if flag:
        print(i,end=" ")