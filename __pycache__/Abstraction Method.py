from abc import ABC
class Engine(ABC):
    
    def Start(self):
        pass
    def Stop(self):
        pass
class PetrolEngine(Engine):
    def Start(self):
        print("Petrol Engine Start")
    def Stop(self):
        print("Petrol Engine Stop")
class DieselEngine(Engine):
    def Start(self):
        print("Diesel Engine Start")
    def Stop(self):
        print("Diesel Engine Stop")
class Car:
    def __init__(self,Engine):
        self.Engine=Engine
    def Start_Engine(self):
        self.Engine.Start()
    def Stop_Engine(self):
        self.Engine.Stop()
P=PetrolEngine()
d=DieselEngine()
c=Car(d)
c.Start_Engine()
c.Stop_Engine()