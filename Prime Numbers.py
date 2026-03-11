def prime_number(n,i,countfact):
    if i*i>n:
        return countfact==2
    if (n%i==0):
        countfact+=1
        if i!=(n//i):
            countfact+=1
    return prime_number(n,(i+1),countfact)
n=int(input("Enter a number:"))
flag=prime_number(n,1,0)
if flag:
    print(f"\nThe {n} is prime")
else:
     print(f"\nThe {n} is not prime")
