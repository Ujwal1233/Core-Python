import pickle
class Employee:
    def __init__(self,id,name,sal,addr):
        self.eid=id
        self.ename=name 
        self.esal=sal
        self.eaddr=addr
    def display(self):
        print(self.eid)
        print(self.ename)
        print(self.esal)
        print(self.eaddr)
f=open("emp","rb")
e=pickle.load(f)
e.display()
f.close()
print("Object is retrieved from saved file")