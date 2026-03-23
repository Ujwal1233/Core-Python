class A:
    def __init__(self):
        self.a=10
    def display(self):
        print("Inside A")
class B(A):
    def display(self):
        print("Inside B")
class C(B):
    def display(self):
        print("Inside C")
class D(C):
    def dispD(self):
        C.display(self)
        B.display(self)
        A.display(self)
d1=D()
d1.dispD()


    