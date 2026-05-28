#inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,"is eating")
class Dog(Animal):
    def bark(self):
        print(self.name,"is barking")
Dog1=Dog("snuffy")
Dog1.eat()
Dog1.bark()

