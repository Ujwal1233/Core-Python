def factors(n,i):
    if i>n:
        return 
    if n%i==0:
        print(i,end=" ")
    factors(n,i+1)
n=int(input("Enter a num:"))
factors(n,1)
