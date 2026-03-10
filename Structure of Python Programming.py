a=10
def fun1():
    print(a)
    b=20
    print(b)
fun1()
def outer():
    global a
    c=30
    def inner():
        print(a)
        c=300
        d=40
    inner()
outer()
class Demo:
    e=50
    def __init__(self):
        self.f=60
        self.g=70
    def disp(self):
        print(self.f)
        h=80
        print(h)
d1=Demo()
print(d1.g)
print(Demo.e)
d1.disp()