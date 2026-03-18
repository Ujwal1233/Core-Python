n=int(input("enter no : "))
for i in range(0,n):
    print(" "*(i),"* "*(n-i))
for i in range(2,n+1):
    print(" "*(n-i),"* "*i)