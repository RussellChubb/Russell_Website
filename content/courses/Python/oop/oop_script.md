# OOP Script

Hey everyone!

Welcome back to the channel.

Today, we’re diving into Object-Oriented Programming (or OOP) in Python. I’m going to cover OOP Syntax, Principles, and when you should, and shouldn’t use it. So, let’s get started!

Object-Oriented Programming is a way of structuring your code so it’s easier to understand, reuse, and maintain. It’s all about creating ‘objects’ that represent real-world things.

These objects can have properties, the example I’ll use to demonstrate this is a car. A car can have properties like a color, make, year and behaviours, like starting the engine or braking.

In Python, we implement OOP using classes and objects. You can think of a class as a kind of blueprint. Let’s create a blueprint for our car.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running!")
```

Here, we’ve defined a class called Car - Oh and just a note, the PEP8 standards define that class names should be capitalized.

One of the biggest things that stumped me when I was first learning about OOP was the use of __init__, as it was the first dunder (or magic) method I’d encountered.

The __init__ method is a special method called a constructor. It runs automatically when we create an object from the class and initializes the object’s properties. Oh btw, a method is a function that takes a class instance as its first parameter - Or the way I like to think of them is functions that live inside of classes.

Another one of the things that tripped me up when I was first learning about OOP was the use of the self parameter in methods. The self parameter refers to the instance of the class that’s being created or accessed.

Think of self as a placeholder for the specific object you’re working with. For example, if you have two car objects, self lets you distinguish between them.

Now, let’s create an object from our Car class.

```python
my_car = Car("Toyota", "Hilux-Surf", 1994)
my_car.start_engine()
```

When we run this, it will output:

```bash
The 1994 Toyota Hilux-Surf’s engine is now running!
```

We can add more methods to our class to give it additional behaviors. For example, let’s add a method to stop the engine.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running!")

    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now off.")
```

Now our car can start and stop its engine.

One of the most powerful features of OOP is inheritance. It allows us to create a new class that inherits properties and methods from an existing class.

```python
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def charge_battery(self):
        print(f"The {self.year} {self.make} {self.model}'s {self.battery_size}kWh battery is now charging.")
```

Here, ElectricCar is a child class of Car. It inherits the start_engine and stop_engine methods but also adds a new method: charge_battery.

Before we wrap up, let’s quickly cover four key principles of OOP: Encapsulation, Abstraction, Inheritance, and Polymorphism.

Encapsulation means bundling data and methods that operate on that data within a single class. It helps protect the internal state of an object from unintended interference. For example, you can use private attributes in Python by prefixing them with an underscore.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
```

Abstraction involves hiding the complex implementation details of a class and exposing only what’s necessary. For example, when you use the start_engine method of a car, you don’t need to know exactly how the engine starts internally.

Inheritance, as we saw earlier, lets us reuse code by creating new classes based on existing ones. This reduces redundancy and improves code organization.

Polymorphism allows us to use a unified interface for different types of objects. For instance, let’s say you have a Shape class with a method draw. Different shapes like Circle and Square can implement their own version of draw, but you can call draw on any shape without worrying about its specific type.

```python
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

class Square(Shape):
    def draw(self):
        print("Drawing a square.")

def render(shape):
    shape.draw()

circle = Circle()
square = Square()
render(circle)  # Output: Drawing a circle.
render(square)  # Output: Drawing a square.
```

Sometimes, when people first learn about OOP, they tend to overuse it. Let’s talk about when you should and shouldn’t use OOP.

Use OOP when:

* Your project involves real-world entities that can be modeled as objects with properties and behaviors. For example, a game with players, enemies, and items.

* You need to reuse code across different parts of your project. Inheritance and polymorphism can save you a lot of effort here.

* You’re working on a large or complex application where organizing code into classes makes it more manageable."

Avoid OOP when:

* You’re building a simple script or a quick one-off solution. A procedural approach is often easier and faster for small tasks.

* Your program doesn’t have much state to manage. For example, a data processing pipeline might not benefit from OOP as much as functional programming.

Overusing OOP can lead to overly complicated designs, making your code harder to read and maintain. Keep it simple!"

So why use OOP? It makes your code more organized, reduces repetition, and makes it easier to debug and extend. Whether you’re building a simple project or a large application, OOP can save you a ton of time and effort.

Thanks for watching! If you found this video helpful, give it a thumbs up and subscribe for more programming tutorials. And if you have any questions or topics you’d like me to cover, drop them in the comments below. See you next time!
