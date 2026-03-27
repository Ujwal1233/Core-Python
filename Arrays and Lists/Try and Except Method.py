n=input("Enter a num")
print(type(n))
print(n)
print("===============")
#An exception is occured when "" is inserted
try:
    n=int(input("Enter a num"))
    print(type(n))
    print(n)
except Exception as e:
    print("Invalid Input")
