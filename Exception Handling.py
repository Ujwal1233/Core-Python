print("Enter a value 1")
a=int(input())
print("Enter a value 2")
b=int(input())
try:
    res=a/b
    print(res)
except Exception as e:
    print("Error in program")
else:
    print("Normally Executed")
print("Program end")