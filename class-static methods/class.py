
class Car:
    base_price = 100000

    def __init__(self,windows,door,power):
        self.windows=windows
        self.door=door
        self.power=power
    
    def what_base_price(self):
        print("The base price is {}".format(self.base_price))

    @classmethod
    def revised_base_price(cls,inflation):
        cls.base_price = cls.base_price + (cls.base_price*(inflation/100))


Car.revised_base_price(10)
print(Car.base_price)       #110000

Car1 = Car(4,5,2000)
print(Car1.base_price)      #110000

Car1.revised_base_price(10)
print(Car1.base_price)      #121000