def countdigits(n,count):
    if n<=0:
        return count
    n=n//10
    count=count+1
    return countdigits(n,count)
num=int(input("Enter a num:"))
res=countdigits(num,0)
print(f"The count of digits in {num} is {res}")