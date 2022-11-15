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
def countDown(n):
    if n < 1:
        return []
    return [n] + countDown(n - 1)

print("List: ", countDown(10))

# tuple,
def studentName(first, last):
    tempTuple = (first[0], last[0])
    return tempTuple

tuple_1 = studentName([1], ["Aliya"])
tuple_2 = studentName([2], ["Zhanerke"])
tuple_3 = studentName([3], ["Almash"])
tuple_4 = studentName([4], ["Ryskeldi"])
tuple_5 = studentName([5], ["Samat"])

print('Students: \n', tuple_1, '\n', tuple_2, '\n', tuple_3, '\n', tuple_4, '\n', tuple_5)

# dictionary.


# Give an example of using the Map,

# Filter,
def filterList(f):
    return f > 10

originalList = [1, 12, 4, 55, 2, 30]
filteringList = list(filter(filterList, originalList))

print("Filtering list: ", filteringList)

# and Reduce functions.