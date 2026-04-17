# class and object 
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)

p1 = person("Ujwal", 30)
p1.display()

# ploymerism

class animal:
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog barks")
class cat(animal):
    def sound(self):
        print("Cat meows")

a = animal()
d = dog()
c = cat()
a.sound()
d.sound()
c.sound()

# inheritance

class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(self.brand, self.model)

class car(vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def display_info(self):
        super().display_info()
        print("Year:", self.year)

my_car = car("Toyota", "Corolla", 2020)
my_car.display_info()

# multiple inheritance

class A:
    def method_a(self):
        print("Method A")
class B:
    def method_b(self):
        print("Method B")
class C(A, B):
    def method_c(self):
        print("Method C")
c = C()
c.method_a()

encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())

# static method

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtils.add(2, 3))
print(MathUtils.multiply(2, 3))

# abstract class
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
circle = Circle(5)
print("Area of circle:", circle.area())