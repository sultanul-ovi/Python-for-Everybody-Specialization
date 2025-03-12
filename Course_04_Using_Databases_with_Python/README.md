# Python For Everybody-Coursera

This course is part of the Python for Everybody Specialization

## [Using Databases with Python](https://www.coursera.org/learn/python-databases?specialization=python)

### About this Course

This course will introduce students to the basics of the Structured Query Language (SQL) as well as basic database design for storing data as part of a multi-step data gathering, analysis, and processing effort. The course will use SQLite3 as its database. We will also build web crawlers and multi-step data gathering and visualization processes. We will use the D3.js library to do basic data visualization. This course will cover Chapters 14-15 of the book “Python for Everybody”. To succeed in this course, you should be familiar with the material covered in Chapters 1-13 of the textbook and the first three courses in this specialization. This course covers Python 3.

**WHAT YOU WILL LEARN**

- Use the Create, Read, Update, and Delete operations to manage databases
- Explain the basics of Object Oriented Python
- Understand how data is stored across multiple tables in a database
- Utilize the Google Maps API to visualize data

## Course Syllabus

**WEEK-1 : Object Oriented Python**

> To start this class out we cover the basics of Object Oriented Python. We won't be writing our own objects, but since many of the things we use like BeautifulSoup, strings, dictionaries, database connections all use Object Oriented (OO) patterns we should at least understand some of its patterns and terminology.

**WEEK-2 : Basic Structured Query Language**

> We learn the four core CRUD operations (Create, Read, Update, and Delete) to manage data stored in a database.

**WEEK-3 : Data Models and Relational SQL**

> In this section we learn about how data is stored across multiple tables in a database and how rows are linked (i.e., we establish relationships) in the database.

**WEEK-4 : Many-to-Many Relationships in SQL**

> In this section we explore how to model situations like students enrolling in courses where each course has many students and each student is enrolled in many courses.

**WEEK-5 : Databases and Visualization**

> In this section, we put it all together, retrieve and process some data and then use the Google Maps API to visualize our data.

---

# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects." These objects can contain data in the form of fields (attributes) and code in the form of methods (functions). Python supports OOP and provides features like class inheritance, encapsulation, and polymorphism.

In this notebook, we will cover:
- Classes and Objects
- Constructors and Instance Variables
- Methods in Classes
- Inheritance
- Encapsulation
- Polymorphism


# Defining a simple class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating an object of the class
car1 = Car("Toyota", "Camry", 2022)
print(car1.display_info())

## Classes and Objects

A **class** is a blueprint for creating objects. It defines attributes (variables) and methods (functions) that operate on the data.

An **object** is an instance of a class, with its own set of attributes.

In the example above:
- The `Car` class has attributes: `brand`, `model`, and `year`
- The `__init__` method initializes these attributes
- The `display_info` method prints car details
- We created an instance `car1` with values

# Creating multiple instances of the Car class
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ford", "Mustang", 2023)

# Displaying information for each car
print(car2.display_info())
print(car3.display_info())

## Instance and Class Variables

Instance variables belong to an instance (object), while class variables are shared across all instances.

class Car:
    # Class variable
    wheels = 4

    def __init__(self, brand, model):
        # Instance variables
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model} with {Car.wheels} wheels"

# Creating objects
car1 = Car("Tesla", "Model 3")
car2 = Car("BMW", "X5")

print(car1.display_info())
print(car2.display_info())

# Changing class variable affects all instances
Car.wheels = 6
print(car1.display_info())
print(car2.display_info())

## Methods in Classes

There are three types of methods in Python classes:
- **Instance Methods**: Operate on instance variables.
- **Class Methods**: Operate on class variables (use `@classmethod`).
- **Static Methods**: Do not modify class or instance variables (use `@staticmethod`).

class Example:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    # Instance method
    def instance_method(self):
        return f"Instance variable: {self.instance_variable}"

    # Class method
    @classmethod
    def class_method(cls):
        return f"Class variable: {cls.class_variable}"

    # Static method
    @staticmethod
    def static_method():
        return "I am a static method"

# Creating an object
obj = Example("Instance Value")

print(obj.instance_method())  # Access instance variable
print(Example.class_method())  # Access class variable
print(Example.static_method())  # Call static method

## Inheritance

Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make sounds"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")

## Encapsulation

Encapsulation restricts direct access to variables, using private variables (`__variable`) and getter/setter methods.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. Remaining balance: {self.__balance}"
        return "Insufficient balance"

    def get_balance(self):
        return f"Current balance: {self.__balance}"

# Creating an account
account = BankAccount(1000)

print(account.deposit(500))
print(account.withdraw(300))
print(account.get_balance())

# print(account.__balance)  # This would raise an AttributeError (private variable)

## Polymorphism

Polymorphism allows different classes to share the same method name but implement it differently.

class Bird:
    def fly(self):
        return "Some birds can fly"

class Sparrow(Bird):
    def fly(self):
        return "Sparrows can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

# Polymorphism example
def flying_ability(bird):
    print(bird.fly())

sparrow = Sparrow()
penguin = Penguin()

flying_ability(sparrow)
flying_ability(penguin)

## Conclusion

Object-Oriented Programming (OOP) in Python provides:
- **Encapsulation**: Restrict access to private variables.
- **Inheritance**: Allow reuse of parent class properties.
- **Polymorphism**: Enable different implementations of the same method.
- **Code Reusability**: Write efficient and modular code.

Using OOP, we can design scalable and maintainable software.

---