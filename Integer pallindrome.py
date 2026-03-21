def int_palindrome(n,rev,temp):
    if n<=0:
        return rev==temp
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return int_palindrome(n,rev,temp)
num=int(input("Integer Pallindrome:"))
flag=int_palindrome(num,0,num)
if flag:
    print(f"{num} is pallindrome")
else:
    print(f"{num} is not pallindrome")

