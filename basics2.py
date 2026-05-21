class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
car1=Car("BMW","Black")
car2=Car("Tesla","White")
print(car1.brand)
print(car2.color)
# start and stop
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def start(self):
        print(self.brand,"is starting")
    def stop(self):
        print(self.brand,"is stopping")
car1=Car("BMW","White")
car1.start()
car1.stop()
