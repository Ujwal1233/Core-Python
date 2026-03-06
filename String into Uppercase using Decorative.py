def print_msg():
    msg="python course"
    return msg
def outer(print1):
    print("Inner outer")
    def inner():
        print("Insude inner")
        ref=print1
        res=ref()
        res1=res.upper()
        print(res1)
        print("Learning inner")
    return inner
ptr1=outer(print_msg)
ptr1()
print("pgm end")