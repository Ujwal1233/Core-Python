print("Enter a value 1")
a=int(input())
print("Enter a value 2")
b=int(input())
try:
    c=a/b
    print(c)
except Exception as e:
    print("Error in program")
print("Program End")