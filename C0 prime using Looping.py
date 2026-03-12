def coprime(n1,n2):
    gcd=0
    while n1>0:
        if n1<n2:
            n1,n2=n2,n1
        n1=n1%n2
    return n2==1
n1=int(input("Enter a first number:"))
n2=int(input("Enter a second number:"))
res=coprime(n1,n2)
if res:
    print(f"The num {n1} & {n2} are co-prime")
else:
    print(f"The num {n1} & {n2} are not co-prime")