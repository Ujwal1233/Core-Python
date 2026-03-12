class Book:
    def __init__(self, value):
        self.__pages = value

    def setter(self, value):
        if value >= 1:
            self.__pages = value

    def getter(self):
        return self.__pages


b1 = Book(100)

b1.setter(114)
res1 = b1.getter()
print(res1)

b1.setter(115)
res1 = b1.getter()
print(res1)