print("Hello World")
# Tuples are indexed by integers 
# Unlike Lists, Tuples are Immutable
# They are comma-separated list of values, syntactically
# To create a tuple with a single element, you have to include a final comma

t1 = 'a', 'b', 'c', 'd', 'e', 'f'
print(type(t1))

t2 = 'a', # class 'tuple'
t3 = 'a'  # class 'str'
print(type(t2), type(t3))

# An Alternative way of creating the tuple is by using the tuple built-in function
# The built-in tuple function takes in only one argument
t4 = tuple()
print(type(t4), t4)

# If the argument is a sequence (string, list or tuple), the result is a tuple with the elements of the sequence:
t5 = tuple('lupins')
# Avoid using tuple as a variable name in python 3.
print(type(t5), t5)

# Most List operators also work on tuples, e.g the bracket operator
t6 = ('a','b', 'c', 'd','e', 'f')
print(t6[0])
# The slice operator also works with a tuple, and is used for selecting a range of elements 
print(t6[1:3])

# The elements of a tuple cannot be modified, You will get a TypeError if you do this. 
# This is because tuples are immutable








