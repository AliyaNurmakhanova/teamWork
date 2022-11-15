# Creating a functional and
z = 0
def increment():
    global z
    z += 1

increment()
print(z)

# non-functional function.
def max2(a, b):
    if a > b:
        return a
    return b
print(max2(2, -3))

# An example of calling a function inside a function.
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

num = 3
print("The factorial of", num, "is", factorial(num))

def max3(a, b, c):
    return max2(a, max2(b, c))

print(max3(2, 7, -3))

# Create a function that returns a list, tuple, dictionary.


# Give an example of using the Map, Filter, and Reduce functions.