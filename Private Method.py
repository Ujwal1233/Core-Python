class Demo:
    def __private_method1(self,a,b):
        return a+b
    def __private_method2(self,a,b):
        return a*b
    def calculate(self):
        add=self.__private_method1(5,10)
        mul=self.__private_method2(10,10)
        print(add)
        print(mul)
d=Demo()
d.calculate()
