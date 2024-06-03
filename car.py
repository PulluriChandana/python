class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def display_info(self):
        print(f"Making of car {self.make},Model of a car {self.model}")

car1=Car("Benz","8")
car2=Car("Mahindra","Grand10")

car1.display_info()
car2.display_info()
