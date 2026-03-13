def fac(n):
    if n<=1:
        return 1
    return n*fac(n-1)
num=int(input("Enter a number:"))
res=fac(num)
print(f"The factor of {num} is {res}")