def square_root(n,i):
    if i*i>n:
        return
    if n%i==0:
        print(i,end=" ")
        if i!=(n//i):
            print((n//i),end=" ")
    return square_root(n,(i+1))
n=int(input("Enter a number:"))
print(f"the  factor of {n} is:")
res=square_root(n,1)
