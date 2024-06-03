class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello,my name is {self.name} and i am {self.age} years old")

#Creating Instances of the class
person1=Person("Chandana",22)
person2=Person("Meghana",24)

#Calling methods
person1.greet()
person2.greet()