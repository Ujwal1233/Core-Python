from threading import Thread
import time
class Task1(Thread):
    def run(self):
        name=["Rama","Krishna","Arjuna"]
        for i in name:
            print(i)
            time.sleep(2)
class Task2(Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(2)
class Task3(Thread):
    def run(self):
        a=10
        b=20
        c=a+b
        print("The sum is",c)
        time.sleep(2)
t1=Task1()
t2=Task2()
t3=Task3()
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Program Ended")