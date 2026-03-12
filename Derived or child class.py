class Parent:
    def __init__(self):
        self.a=10
class child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b=20
cf=child()
print(cf.b)
print(cf.a)
