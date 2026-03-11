class Person:
    def __init__(self):
        self.__name=' '
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
    getset=property(getter,setter)
P=Person()
P.getset=("Ujwal")
res=P.getset
print(res)
