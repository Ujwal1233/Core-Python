class Radio:
    def turnOn(self,x):
        if(x==1):
            print("Radio is on")
        else:
            print("Radio is off")
class Car:
    def __init__(self,min,max):
        self.Cmin=min
        self.Cmax=max
        self.r=Radio()
c=Car(60,120)
print(c.Cmin)
print(c.Cmax)
c.r.turnOn(1)
c.r.turnOn(2)