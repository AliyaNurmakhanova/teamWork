# Creating a non-functional and
z = 0
def increment():
    global z
    z += 1

increment()
print(z)

# functional function.
def max2(a, b):
    if a > b:
        return a
    return b
print("Max of this two numbers: ", max2(2, -3))

# An example of calling a function inside a function.
def max3(a, b, c):
    return max2(a, max2(b, c))

print("Max of this three numbers: ", max3(2, 7, -3))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

num = 3
print("The factorial of", num, "is", factorial(num))

# Create a function that returns a list,

# tuple,

# dictionary.


# Give an example of using the Map,

# Filter,
def filterList(f):
    return f > 10

originalList = [1, 12, 4, 55, 2, 30]
filteringList = list(filter(filterList, originalList))
print("Filtering list: ", filteringList)
# and Reduce functions.