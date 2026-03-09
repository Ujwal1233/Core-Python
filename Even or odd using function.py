def isEVENODD(n):
    return n%2==0
    #     return True
    # else:
    #     return False
n=int(input("Enter a number:"))
flag=isEVENODD(n)
if flag:
    print(f"{n} is Even num")
else:
    print(f"{n} is Odd num")