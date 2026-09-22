# Control Flow

Hey guys!

Today, we're exploring control flow statements in Python.

We’re going to be looking at if, elif (or 'else if'), and else. Let’s get into it!

## First Code Block (If)

This code takes an input number for x and checks if it’s greater than or equal to 18.If it is, it prints a message. Otherwise… nothing happens.

```python
# "if" Demo
x = int(input("What do you want x to be?"))

if x >= 18:
    print(f"{x} is greater than or equal to 18")

else:
x = int(input("What do you want x to be?"))

if x >= 18:
    print(f"{x} is greater than or equal to 18")

else:
    print(f"{x} is not greater than or equal to 18")
```

However, what happens if a user wants to evaluate a number < 18? We don’t have any logic in the code to handle this?

The way we can handle this, is by inserting an else statement, which catches all other cases, including if a user inputs a number < 18.

I mentioned in a previous video that code executes programmatically, from top to bottom

```python
elif (errors):
x = int(input("What do you want x to be?"))

if x >= 18:
    print(f"{x} is greater than or equal to 18")

elif x == 24:
    print(f"{x} is 24 :O")

else:
    print(f"{x} is not greater than or equal to 18")
```

Fix

```python
x = int(input("What do you want x to be?"))

if x == 24:
    print(f"{x} is 24 :O")

elif x >= 18:
    print(f"{x} is greater than or equal to 18")

else:
    print(f"{x} is not greater than or equal to 18")
```

## Or statement

```python
name = str(input("What's your name?"))

if name == "Russell":
    print(f"Sup {name}")

elif name == "Russell" or name == "Olivia":
    print(f"Suhhhhhhhhhhhhh")

else:
    name != "Russell"
    print("What's your vibe bro?!")
```
