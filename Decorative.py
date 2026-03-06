def print_msg():
    print("Hellon Everyone")
def outer(print1):
    print("Entering Outer")
    def inner():
        print("Entering Inner")
        ref=print1
        ref()
        print("Leaving inner")
    print("calling inner")
    return inner
ptr1=print_msg
ptr2=outer(ptr1)
ptr2()
print("program end ")