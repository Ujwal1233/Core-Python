def outer():
    print("Inside Outer")
    def inner():
        print("Inside inner")
    return inner
ref=outer()
print(ref)
ref()