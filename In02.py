class A:
    def __init__(self):
        self.a1=10
class B:
    def __init__(self):
        A.__init__(self)
        self.b1=20
class C(B):
    def __init__(self):
        B.__init__(self)
        self.c1=30
cf=C()
print(cf.c1)
print(cf.b1)
print(cf.a1)