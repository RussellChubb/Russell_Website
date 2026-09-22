# Loops Script

In Python, loops are control flow statements that allow us to repeat a block of code as long as certain conditions are met.

So, what does that even mean? Well, first off, there are two kinds of loops in Python, while loops, and for loops.

Starting with while loops, which are defined by using the while keyword, these loops repeat their block until a given condition is satisfied.

```python
# To infinity, and BEYOND!
condition = True

while condition == True: 
 print("The condition is True") 
```

For example, this code-snippet will repeat to infinity, as we never alter the initial condition to cause the loop to stop.

I’d highly encourage you to execute this command block in your IDE, and actually take a look at what the output says.

Also, I’m now going to be using the Dracula VS-Code Theme, so all syntax coloring I do in this video (And likely the next few) will be to that theme. If you don’t understand what that means, it doesn’t matter - Let’s continue!

Alright, now that we’ve created an infinite loop, let's add a condition to stop the loop after the first loop iteration.

```python
# We're not aiming for the truck!
condition = True 

while condition == True: 
 print("The condition is True")     
 condition = False 
   print("Loop Ended") 
```

The reason this extra line stops the loop is because initially the variable “condition” is equal to True.

However, as the code runs sequentially from top to bottom,  after 1 iteration of the loop, we can see that the variable “condition” gets updated to false. And because the loop is conditional, on the variable “condition” being true, the loop stops.
It’s very common when using while loops to have some sort of counter declared as a variable, for example, in this code snippet, we have declared a variable count, with an integer value of 0.

```python
# Using a counter, and f strings, and assignment operators - woo hoo
count = 0 

while count < 10:     
 print(f"The condition is True | Count = {count}")
 count += 1
print("Loop Ended")
```

After each iteration of the loop, we increase the value of the variable “count” by 1, which continues until the count is equal to 10, where-in because the condition is now false, the loop ends, and the “Loop Ended” text is printed to the screen.

Also, if you don’t understand what’s happening on line # 6, feel free to watch my previous video, on operators in Python, to get a better understanding of what's happening here.

Now, let’s talk about for loops, which allows us to tell Python that we want to execute a code block a predetermined amount of times, without the need to create a separate variable, and condition to check the value.

For example, with for loops, we can iterate over items in a list:

```python
# Basic List Iteration
list = [1, 2, 3, 4] 

for item in list:     
     print(item) 
```

Or we can pass in a value to the range() function, to specify the number of times we want the loop to iterate.

```python
# I miss Vine
For x in range(5):
        print("suh dude")
```

Up until this point I haven’t discussed break, or continue statements, which allow you to control the flow of your loops. For example, when using the break statement, you can iterate over a list to find a certain value within the list.

For example, in this code-snippet, you can iterate over the list “dudes”, until you find a certain value within this list, in this case, we want the loop to “break” when “person” is equal to Liam.

```python
# Shout out to my Hataitai Battlers
dudes = ["Ben", "Liam", "Sean"]
for person in dudes:
        print(person)
        if person == "Liam':
                break
```

You can use the continue statement to stop the current iteration of a loop and continue with the next. For example in this code snippet, we can get our loop to continue, even after item “Liam” has been found.

```python
# I don't really use continue much
dudes = ["Ben", "Liam", "Sean"]
for person in dudes:
        print(person)
        if person == "Liam":
                Continue
print(person)
```

That’s it for my introduction to Loops in Python. I hope you had fun in this lesson, as loops were one of the first concepts that really attracted, and intrigued me in the world of programming.

Feel free to leave any questions in the comments, as I read through all of them! As well as questions, feel free to leave any suggestions on topics, or videos you’d like me to cover.

And if you’re following along the series, continue to tune in, as we’re going to start taking a few steps towards slightly more “intermediate” programming in Python.

Thanks for watching, if you like the video, like the video, if you want to see more of me, press subscribe.

Cheers
