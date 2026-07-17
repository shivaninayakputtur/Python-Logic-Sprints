from abc import ABC,abstractmethod
class shape(ABC):
    def area(self):
        pass
class circle(shape):
    def area(self):
        print("calculating cirlce area")
class rectangle(shape):
    def area(self):
        print("calculating rectangle area")
r=rectangle()
r.area()
c=circle()
c.area()