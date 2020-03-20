from carss import Car

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Batter()

class Batter():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery")

    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270

        message="This car can go approximately"+str(range)+" miles on a full charge."
        print(message)

my_new_car=Car('audi','a4',2010)
print(my_new_car.get_descriptive_name())

my_tesla=ElectricCar('tesla','model_s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()