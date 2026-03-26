try:
    print("Enter a value 1")
    a=int(input())
    print("Enter a value 2")
    b=int(input())
    c=a/b
    print(c)
except ValueError as e:
    print("It is value error")
except ZeroDivisionError as e:
    print("It is a ZerodivisionError")
except Exception as e:
    print("It is a error")
    print(e)
print("Program end")