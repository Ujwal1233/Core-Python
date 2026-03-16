class Os:
    def __init__(self):
        self.status=True
        print("Os is installing")
    def getOs(self):
        print("Os is still installing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=Os()
        print("Mobile is created")
        print("With Os installed")
m=Mobile("iphone")
print(m.mname)
print(m.o.status)
m.o.getOs()
del m
print("After del")
print(m.mname)
print(m.o.status)

