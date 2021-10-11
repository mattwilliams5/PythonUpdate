"""
Primitive Data Types
"""

name = "Matt"  # Storing a string value
age = 44  # Storing a Integer value
cash = 100.25  # Storing a Float
retired = False  # Storing a Boolean value

# How to know the Data Type of a variable
# Invoking the function 'type (<VARIABLE NAME>)'
print("Data Type of the variable 'name' is", type(name))
print("Data Type of the variable 'age' is", type(age))
print("Data Type of the variable 'cash' is", type(cash))
print("Data Type of the variable 'retired' is", type(retired))


"""

Composite Data Types
"""

nucamp_locations = ["Seattle", "Tacoma", "Bellevue"]  # Storing a List
Matt_Info = {"name": "Matt", "age": 44, "cash": 100.25,
             "retired": False}  # Storing a Dictionary
my_tuple = ("apple", "banana", "cherry")  # Storing a Tuple
my_set = {"cats", "dogs", "birds"}  # Storing a Set

print(" ")
print("Data Type of the variable 'nucamp_locations' is", type(nucamp_locations))
print("Data Type of the variable 'Matt_Info' is", type(Matt_Info))
print("Data Type of the variable 'my_tuple' is", type(my_tuple))
print("Data Type of the variable 'my_set' is", type(my_set))
print(Matt_Info["name"])
