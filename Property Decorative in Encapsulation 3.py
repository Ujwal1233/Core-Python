class Student:
    def __init__(self):
        self.__name=" "
    def getset(self):
        return self.__name
    def getset(self,value):
        self.__name=value
s=Student()
s.getset="rama"
r1=s.getset
print(r1)