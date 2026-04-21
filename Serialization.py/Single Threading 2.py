import time
class Demo:
    def print_names(self):
        name=["Rama","Krishna","Arjuna"]
        for i in name:
            print(i)
            time.sleep(2)
    def print_num(self):
        for i in range(10):
            print(i)
            time.sleep(2)
    def sum(self):
        a=10
        b=20
        c=a+b
        print("The sum is",c)
        time.sleep(2)
d1=Demo()
d1.print_names()
d1.print_num()
d1.sum()
print("Program Ended")