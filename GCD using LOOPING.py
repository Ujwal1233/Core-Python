def GCD(n1,n2):
    hcf=0
    while n1>0:
        if n1<n2:
            n1,n2=n2,n1
        n1=n1%n2
        n2=n2
    return n2
n1=int(input("Enter a first number:"))
n2=int(input("Enter a second number:"))
res=GCD(n1,n2)
print(f"The gcd of {n1} & {n2} is {res}")

                    