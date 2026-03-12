def gcd(n1,n2):
    if n1==0:
        return n2
    if n1<n2:
        n1,n2=n2,n1
    return gcd((n1%n2),n2)
n1=int(input("Enter a first number:"))
n2=int(input("Enter a second number:"))
res=gcd(n1,n2)
print(res)