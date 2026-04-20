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
e=Employee(101,"Ujwal",100,"Banglore")
f=open("emp","wb")
pickle.dump(e,f)
f.close()
print("object is saved into the text file")