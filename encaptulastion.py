class Account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance =balance

    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        self.__balance=amount
acc1=Account("shivani",50000000)
print(acc1.get_balance())
acc1.set_balance(800000000)
print(acc1.get_balance())