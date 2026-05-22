class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=40:
            print(self.name,"is passed")
        else:
            print(self.name,"is failed")
student1=Student("shivani",99)
student1.result()