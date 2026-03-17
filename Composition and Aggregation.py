class Engine:
    def __init__(self):
        self.type = "Petrol"
        print("Engine is created")

    def start(self):
        print("Engine is starting...")
class Driver:
    def __init__(self, name):
        self.name = name
        print("Driver is ready")

    def drive(self):
        print(self.name, "is driving the car")
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()
        self.driver = None
        print("Car is ready with engine")
    def assign_driver(self, driver_obj):
        self.driver = driver_obj
        print("Driver assigned to car")
c = Car("Toyota")
print(c.brand)
c.engine.start()
d = Driver("Deepak")
c.assign_driver(d)
print(c.driver.name)
c.driver.drive()