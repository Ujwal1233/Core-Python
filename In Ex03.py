class Animal:
    def eat(self):
        print("Animal is Eating")
    def breath(self):
        print("Animal is Breathing")
    def sleep(self):
        print("Animal is Sleeping")
class Tiger(Animal):
    def eat(self):
        print("Tiger will Hunt & eat")
class Deer(Animal):
    def eat(self):
        print("Deer will graze & eat")
class Monkey(Animal):
    def eat(self):
        print("Tiger will Steal & eat")
t=Tiger()
d=Deer()
m=Monkey()
t.eat()
t.sleep()
t.breath()
d.eat()
d.sleep()
d.breath()
m.eat()
m.sleep()
m.breath()