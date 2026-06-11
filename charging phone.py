class Phone:
    def __init__(self,brand,battery):
        self.brand=brand
        self.__battery=battery
    def charge(self):
        print(self.brand,"is charging")
    def get_battery(self):
        return self.__battery
    def set_battery(self,charger):
        self.__battery=charger
phone1=Phone("Iphone","Icharger")
phone1.charge()
print(phone1.get_battery())
phone1.set_battery("Samsung")
print(phone1.get_battery())