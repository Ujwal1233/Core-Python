class Plane:
    def takeoff(self):
        print("Plane is takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
class Cargo(Plane):
    def carryg(self):
        print("Plane carry goods")
class Passenger(Plane):
    def carryp(self):
        print("Plane carry Passengers")
class Fighter(Plane):
    def carryw(self):
        print("Plane carry Weapons")
c=Cargo()
p=Passenger()
f=Fighter()
c.takeoff()
c.fly()
c.land()
c.carryg()
p.takeoff()
p.fly()
p.land()
p.carryp()
f.takeoff()
f.fly()
f.land()
f.carryw()