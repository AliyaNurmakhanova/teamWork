# Creating a functional and
a = 0
def increment():
    global a
    a += 1

increment()
print(a)

# non-functional function.
def increment2(x):
    return x + 1
print(increment2(3))

# An example of calling a function inside a function.
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

num = 3
print("The factorial of", num, "is", factorial(num))

# Create a function that returns a list, tuple, dictionary.


# Give an example of using the Map, Filter, and Reduce functions.
