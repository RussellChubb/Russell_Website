# Python Classes

Today we're going to be looking at **classes in Python**.

Classes are one of those things that can seem a little confusing at first, but the basic idea is actually pretty simple.

A class is essentially a **template for creating objects**.

It lets us bundle data and functions together into a single object, which makes it easier to organise and work with related information.

Lots of people use dogs as examples to demonstrate classes, but I think that's overdone, so today we're going to be using cars.

The greatest car ever assembled.

Let's start by creating a really simple class.

In Python, we use the `class` keyword, followed by the name of our class.

```python
class HiluxSurf:

    make = "Toyota"
    model = "Hilux Surf"
    year = 1994
```

Here we've created a class called `HiluxSurf`.

Inside the class, we've defined three attributes:

* `make`
* `model`
* and `year`.

These are **class attributes**, which are properties that are shared by every `HiluxSurf` object we create.

So we've basically created a blueprint that says:

> Every Hilux Surf is a Toyota, it's a Hilux Surf, and in our completely arbitrary example, it's from 1994.

But a class by itself isn't particularly useful, as we need to actually create an object from it.

An **object** is a specific instance of a class. So if `HiluxSurf` is our blueprint, an individual Hilux Surf is an object created from that blueprint.

We can create one like this:

```python
surf1 = HiluxSurf()
```

And now we can access its attributes:

```python
print(surf1.make)
print(surf1.model)
print(surf1.year)
```

Which gives us:

```text
Toyota
Hilux Surf
1994
```

So we've created an object called `surf1` from our `HiluxSurf` class. And we can create as many objects as we want from the same class.

But there's a problem.... What if we want two Hilux Surfs that aren't exactly the same?

Maybe one is red, and another is baby blue.

This is where things get a little more interesting.

We can use the `__init__()` method to initialise an object when it's created. Let's modify our class.

```python
class HiluxSurf:

    make = "Toyota"
    model = "Hilux Surf"
    year = 1994

    def __init__(self, colour, engine):

        self.colour = colour
        self.engine = engine
```

Now, when we create a `HiluxSurf`, we have to provide a colour and an engine.

So we can create two different objects:

```python
surf1 = HiluxSurf("Red", "3.0L Diesel")

surf2 = HiluxSurf("Baby Blue", "2.4L Diesel")
```

And now each object has its own colour.

```python
print(surf1.colour)
print(surf2.colour)
```

Which gives us:

```text
Red
Baby Blue
```

Both objects were created from the exact same class.

But they have different **instance attributes**.

---

## What is `self`?

This is probably the part that looks the strangest when you first encounter classes in Python.

So, what exactly is `self`?

`self` refers to the **current object**.

When we write:

```python
self.colour = colour
```

we're essentially saying:

> Take the value of `colour` that was passed into this object, and store it as this object's colour.

So when we create:

```python
surf1 = HiluxSurf("Red", "3.0L Diesel")
```

Python creates a new `HiluxSurf` object.

Inside that object:

```python
self.colour
```

refers to `surf1`.

So we end up with:

```python
surf1.colour
```

being:

```text
Red
```

Then when we create:

```python
surf2 = HiluxSurf("Baby Blue", "2.4L Diesel")
```

`self` refers to `surf2` instead.

So:

```python
surf2.colour
```

is:

```text
Baby Blue
```

The important thing to remember is that **`self` refers to the particular instance we're currently working with**.

---

## `__str__()`

There's one more useful method I want to show you: `__str__()`.

By default, if we try to print an object:

```python
print(surf1)
```

Python gives us something that looks a bit like this:

```text
<__main__.HiluxSurf object at 0x00000123>
```

Nice.

Not really.

Fortunately, we can tell Python how we want our object to be represented as a string.

We do that by defining our own `__str__()` method.

```python
class HiluxSurf:

    make = "Toyota"
    model = "Hilux Surf"
    year = 1994

    def __init__(self, colour, engine):

        self.colour = colour
        self.engine = engine

    def __str__(self):

        return f"{self.year} {self.make} {self.model} - {self.colour}, {self.engine}"
```

Now we can create our two objects again:

```python
surf1 = HiluxSurf("Red", "3.0L Diesel")

surf2 = HiluxSurf("Baby Blue", "2.4L Diesel")
```

And print them:

```python
print(surf1)
print(surf2)
```

Which gives us:

```text
1994 Toyota Hilux Surf - Red, 3.0L Diesel
1994 Toyota Hilux Surf - Baby Blue, 2.4L Diesel
```

Much better.

When we call:

```python
print(surf1)
```

Python automatically calls the object's `__str__()` method.

So instead of Python giving us that ugly default object representation, we've told it exactly how we want our object displayed.

---

## Recap

So, to recap, a **class** is a blueprint or template for creating objects.

We define a class using the `class` keyword.

```python
class HiluxSurf:
    ...
```

We can create an **object**, or instance, from that class:

```python
surf1 = HiluxSurf()
```

We can use `__init__()` to initialise each object with its own data:

```python
def __init__(self, colour, engine):
    self.colour = colour
    self.engine = engine
```

`self` refers to the particular object we're working with.

And finally, we can use methods like `__str__()` to define how our objects behave or are represented.

Classes are a really important part of Python because they allow us to bundle **data and behaviour** together into reusable objects.

And hopefully, by now, you've got a slightly better understanding of how they work.

And, more importantly, you now know that the correct way to learn Python classes is obviously by creating a fleet of 1994 Toyota Hilux Surfs.
