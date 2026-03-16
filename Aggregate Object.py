class Charger:
    def __init__(self,name):
        self.cname=name
        print("Charger is Ready")
    def getCharger(self):
        print("Charger is used for Charging")
class Mobile:
    def __init__(self,name):
        self.mname=name  
        self.c1=" "
        print("Mobile is ready")
    def hasmobile(self,c):
        self.c1=c
        print("Both charger and mobilr is connected")
m=Mobile("iphone")
charge=Charger("Iphone charger")
m.hasmobile(charge)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()
del m
print(charge.cname)
charge.getCharger()
