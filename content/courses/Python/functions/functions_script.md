# Functions Script

In Python, a function is a block of code that performs a specific task, and allows you to reuse code without rewriting it. You can think of them as mini-programs that can be called whenever needed.

Python has a bunch of built-in functions, like print(), but you can also define your own functions to suit your needs.

Let’s take a look at how to define a function in Python. To create a function, we use the def keyword, followed by the function name, parentheses, and a colon. Inside the function, we include the code that we want to execute whenever the function is called.

```python
def greet():
    print("Hello, world!")
```

Here, we have a function called greet() that, when called, will simply print "Hello, world!" to the screen.
To run the code inside a function, you need to call the function by using its name followed by parentheses. So, if we type:

```python
greet()
```

We’ll see “Hello, world!” printed to the screen. Simple, right?

Now, functions can also accept parameters, which are values you pass to the function to customize its output. For example:

```python
def greet(name):
    print(f"Hello, {name}!")
```

Here, our greet() function takes a parameter called name. When we call the function, we can specify a value for name, like this:

```python
greet("Russell")
```

This will output “Hello, Russell!” You can think of parameters as placeholders that allow functions to handle different data inputs.

Often, you’ll want your function to return a result. For that, we use the return statement. For example:

```python
def add(a, b):
    return a + b
```

When we call:

```python
add(5, 3)
```

the function returns 8, which we can then use elsewhere in our code.
Let’s combine everything we’ve learned.

Here’s a function that calculates the area of a rectangle:

```python
def calculate_area(length, width):
    return length * width
```

If we call:

```python
calculate_area(10, 5)
```

the function returns 50. This is a great example of how functions can help keep our code modular and organized.
If you like the video, like the video - If you want to see more of me, press subscribe!
