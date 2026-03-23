# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#         self.engine = Engine()
#         self.driver = None
#         print("Car is ready with engine")
#     def assign_driver(self, driver_obj):
#         self.driver = driver_obj
#         print("Driver assigned to car")
# class Engine:
#     def __init__(self):
#         self.type = "Petrol"
#         print("Engine is created")
#     def start(self):
#         print("Engine is starting...")
# class Driver:
#     def __init__(self, name):
#         self.name = name
#         print("Driver is ready")
#     def drive(self):
#         print(self.name, "is driving the car")
# c = Car("Toyota")
# print(c.brand)
# c.engine.start()
# d = Driver("Deepak")
# c.assign_driver(d)
# print(c.driver.name)
# c.driver.drive()


class Heart:
    def __init__(self,name):
        self.hname=name
        print("Heart is alive")
    def getheart(self):
        print("Heart is pumping")
class car:
    def __init__(self,name):
        self.cname=name
        print("The car is ready")
    def getcar(self):
        print("Car is ready to drive")
class Person:
    def __init__(self,name):
        self.pname=name
        self.h=Heart("Ujwal")
        self.c1=" "
        print("Person is ready")
        print("With heart connected")
    def hasPerson(self,c):
        self.c1=c
        print("p & h is connected")

p=Person("Ujwal")
cf=car("Ducati")
p.hasPerson(cf)
print(p.pname)
print(p.c1.cname)
print(p.h.hname)
p.h.getheart()
p.c1.getcar()
del p  
print(cf.cname)
cf.getcar()
