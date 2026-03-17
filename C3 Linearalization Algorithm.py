class A:
    def dispA(self):
        print("A")
print(A.mro())
class B:
    def dispB(self):
        print("B")
print(B.mro())
class C(A,B):
    def dispB(self):
        print("C")
print(C.mro())