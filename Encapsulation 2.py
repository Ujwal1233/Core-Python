class Person:
    def __init__(self):
        self.__name=' '
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
P=Person()
P.setter("Ujwal")
res=P.getter()
print(res)
