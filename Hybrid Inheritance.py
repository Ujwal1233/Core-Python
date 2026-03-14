class A:
    def dispA(self):
        print("A")
class B(A):
    def dispB(self):
        print("B")
class C(A):
    def dispC(self):
        print("C")
class D(B,C):
    def dispD(self):
        print("D")