# class Factory:
#     def __init__(self, material, zip, pockets):
#         self.material = material
#         self.zip = zip
#         self.pockets = pockets

#     def show(self):
#         print(f"Your objects details are as follows: Material - {self.material}, Zip - {self.zip}, Pockets - {self.pockets}")
        
# nike = Factory("cotton", 3, 5)
# reebok = Factory("leather", 2, 4)

# print(nike.pockets)  
# print(reebok.material)  

# nike.show()

# class Animal():
#     def __init__(self, age):
#         self.age = age
        
#     def show(self):
#         print(f"This animal is {self.age} years old.")
        
#     @classmethod
#     def create_puppy(cls):
#         return cls(5)  
    
#     @staticmethod
#     def bark():
#         print("Woof! Woof!")   

# dog = Animal(15)
# dog.show()
# dog.create_puppy().show()

# -------------------------------------------------
# Inheritance Example
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")
    
# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
    
#     def show(self):
#         print(f"{self.name} is {self.age} years old.")

# human = Human("Alice",18)
# human.speak()
# human.show()


# Multiple Inheritance Example----------------

# class Father:
#     def __init__(self, name):
#         self.name = name
#         print("I enjoy gardening.")

# class Mother:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("I enjoy cooking.")

# class Child(Mother, Father):
#     def sports(self):
#         print("I enjoy sports.")

# c = Child("John", 12)
# print(c.name)
# c.sports()


# Multilevel Inheritance Example--------------


# class Factory:
#     def __init__(self, material, zip):
#         self.material = material
#         self.zip = zip

# class BhopalFactory(Factory):
#     def __init__(self, material, zip, color):
#         super().__init__(material, zip)
#         self.color = color

# class MumbaiFactory(BhopalFactory):
#     def __init__(self, material, zip, color, pockets):
#         super().__init__(material, zip, color)
#         self.pockets = pockets

# mumbai = MumbaiFactory("leather", 3, "black", 5)
# print(mumbai.material)




# ------------------------------------------------------------------------

# Polymorphism Example

# Method Overriding
# class Animal:
#     def speak(self):
#         print("Animal makes a sound.")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks.")

# dog = Dog()
# dog.speak()  # Output: Dog barks.


# ----------------------------------------------------------------------------

# Encapsulation 

# Protected -> "_" use but not recommended to access outside class
# Private -> "__" not accessible outside class

# class BankAccount:
#     __a = 5000
    
#     def show():
#         print("Welcome to the bank!")
    
    
#     def show2(self):
#         print(self.__a)

# obj = BankAccount()
# obj.show2()

# Example of Protected and Private members--------------------------------

# class Demo:
#     def __init__(self):
#         self.name = "MODI"
#         self._age = 25
#         self.__salary = 50000
    
#     def show(self):
#         print("Public : ", self.name)
#         print("Protected : ", self._age)
#         print("Private : ", self.__salary)

# d = Demo()
# d.show()
# print(d._Demo__salary)   



# ------------------------------------------------------------------------

# Abstraction Base Class Example

# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass
    
# class Circle(abstract):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius   

# obj = Circle(5)
# print(obj.radius)
# print("Area :", obj.area())
# print("Perimeter :", obj.perimeter())





# ------------------------------------------------------------------------

# Dunder Methods Example

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
    
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
    
#     def __del__(self):
#         print(f"The book '{self.title}' has been deleted.")
        
# # book = Book("Rich Dad Poor Dad", "Robert T. Kiyosaki")
# book2 = Book("Eat That Frog!", "Brian Tracy")
# print(book2)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Animal Name: {self.name}, Age: {self.age}"
    
    def __add__(self, other):
        sum = 0
        for i in other:
            sum += i.age
            
        return self.age + sum

obj1 = Animal("Tiger", 15)
obj2 = Animal("Lion", 35)
obj3 = Animal("Fox", 30)
print(obj1)
print(obj2)
print(obj3)
print("Combined Age:", obj1 + (obj2, obj3))