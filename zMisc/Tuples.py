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
# But a tuple can be replaced with another 

t7 = ('A',) + t6[1:] # This statement makes a new tuple and then makes t7 refer to it
print(t7) 


# Relational operators work with tuples, it works by comparing the 
# first element from each sequence, if equal it moves on to the next 
# elements, and so on until it finds the elements that differ.
print((0, 1, 2) < (0, 3, 4)) # True
print((0, 1, 2000000) < (0, 3, 4)) # True
    
# Tuple assignment

a = 100
b = 200
print(a, b) # 100, 200
# value reassignment using tuples
a, b = b , a
print(a, b)  # 200, 100

# Tuples as return values from
# built-in function divmod takes in two arguments and
# returns the quotient and remainder and the result can be 
# stored as a tuple 

t8 = divmod(7, 3)
print(t8)
# Or we can use tuple assignment to store the results separately:
quot, rem = divmod(67, 9)
print(quot)
print(rem)


# Variable-length argument tuples 
"""Functions can take a variable number of arguments. 
A parameter name that begins with
*gathers arguments into a tuple. 
For example, printall takes any number of arguments
and prints them:"""


def printall(*args):
    print(args)


# The gather parameter is similar to the spread operator in javascript
# and is can have any name, burt args is conventional
# calling printall function
printall(1, 'a', 'b', 3, True)
"""
The complement of gather is scatter. If you have a sequence of values and you want to pass
it to a function as multiple arguments, you can use the * operator. For example, divmod
takes exactly two arguments; it doesn’t work with a tuple:
i.e t=(7,3); divmod(t) -> This does not work
But if you scatter the tuple it works as expected.
"""
to1 = (90 , 7)
to2 = (90 , 7, 8, 9)
print(divmod(*to1))
print(sum(to2))


def small(*args):
    return sum(args)
    

print(small(1,2,3,4,5,6,7,8))

# sum(1,2,3,4,5,6,7,8) -> won't work because sum takes at most two arguments and 8 are given here, using the gather operator solves this.



# Lists and Tuples
# The zip function is a built-in function that takes two or more
# sequences and returns a list of tuples where each tuple contains one
# element from each sequence.
# The name of the function refers to zipper, which joins and interleaves two rows of teeth.


# zipping a string and a list 
str__1 = 'abcde'
lis__1 = [0,1,2,3,4]
zip(str__1,lis__1)
print(zip(str__1,lis__1)) # This results in a zip object that knows how to iterate through the pairs.


# The most common use of zip is in a for loop that

for pair in zip(str__1,lis__1):
    print(pair)


"""
A zip object is a kind of iterator, which is any object that iterates through a sequence.
Iterators are similar to lists in some ways, but unlike lists, you can’t use an index to select an element from an iterator.
If you want to use list operators and methods, you can use a zip object to make a list:
"""
print(list(zip(str__1,lis__1)))
# The result would be a list of tuples that contain characters from 
# both the string and the list.
# print(list((1,2,3,4,5,6,7,8)))

# if not the same length the result has the length of the shorter one
for i in zip('john', 'granada'):
    print(i)
    

print(list(zip('john', 'maryanne')))

# Tuple assignment can be used in a for loop to traverse a list of tuples
t9 = [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]
for letter, number in t9:
    print(number, letter)        


"""
If you combine zip, for and tuple assignment, you get a useful idiom for traversing two (or more) sequences at the same time. For example, has_match takes two sequences, t1
and t2, and returns True if there is an index i such that t1[i] == t2[i]:
"""
list_10 = ['a', 'b', 'c', 'd', 'e']
list_20 = ['apple', 'B', 'cow', 'D', 'e']
list_30 = ['apple', 'bee', 'corn', 'dogs', 'enter']
list_40 = [1,2,3,4,5,6,7,8,9]
def has_match(t1,t2):
    for x , y in zip(t1,t2):
        if x == y:
            return True
    return False

print(has_match('james','john'))
print(has_match(list_10, list_20))
print(has_match('zicko','annabel'))
print(has_match(list_30, list_40))

# The built in function Enumerate
# If you need to traverse the elements of a sequence and their indices,
# you can use the built-in function enumerate:
def enum_func():
    print('\n')
    for index, element in enumerate('abcde'):
        print(index, element)# strings
    print('\n')
    for index, element in enumerate(['f','g','h','i','j']):
        print(index, element)   # lists
    print('\n')
    for index, element in enumerate((1,2,3,4,5)):
        print(index, element)   # tuples
    print('\n')
    for index, element in enumerate({'a':1,'b':2,'c':3,'d':4}):
        print(index, element)   # dictionaries

enum_func()



# Dictionaries and Tuples 
# Dictionaries have a method called items that returns a sequence of
# tuples, where each tuple is a key-value pair
# Using a dictionary to initialize a tuple
dic = {'a': 1, 'b': 2, 'c': 3}
t10 = dic.items()
print("THis is t10 ",t10)

# This results in a dict_items object which is an iterator like the
# zip object and it iterates the key-value pairs.
# it can be used in a for loop like this 
for key, value in dic.items():
    print(key, value)


# A list of tuples can be used to initialize a dictionary
dic_2 = dict(t9)
print(dic_2)

# A concise way to create a dictionary is to use the dict constructor
# and the zip method
# Using zip method to make a dictionary 
dic_3 = dict(zip('abc', range(3))) # string -> range
print(dic_3)
dic_4 = dict(zip('james', 'mary')) # string -> list
print(dic_4)
dic_5 = dict(zip(['ronaldo', 'messi', 'benzema','ramos','lewandowski'],[5,6,0,0,1])) # list -> list
print(dic_5)
dic_6 = dict(zip(['bugatti', 'tesla'],'124')) # list -> string
print(dic_6)
dic_7 = dict(zip((3,2,1),('a','b','c'))) # tuple -> tuple
print(dic_7)



# Using tuples as keys in a dictionary 
"""
It is common to use tuples as keys in dictionaries (primarily because you can’t use lists -> (mutable)). 
For example, a telephone directory might map from last-name, first-name pairs to telephone numbers. 
Assuming that we have defined last, first and number, we could write:
directory[last, first] = number
The expression in brackets is a tuple. We could use tuple assignment to traverse this dictionary.
"""
dic_8 = dict(zip(([('james','bond'), ('leroy', 'sane'), ('james','milner')]),[56430, 32328, 23553])) # tuple -> tuple
print(dic_8)

realnames = zip(('a','b','c'),('john', 'kris', 'famok'))
for i in realnames:
    print(i)    
    
dic_9 = dict(zip((('a','b'),('c','d'),('e','f')), [21332,12131,12134])) # tuple )-> tuple
print(dic_9)
print(dic_9.get(('a','b') , 0))



tnames = ('Cleese', 'John'), ('Aubrey', 'Graham'), ('Icahn', 'Eric'), ('Gilliam', 'Jerry'), ('Jones', 'Terry'), ('Palin', 'Michael')

# for first , last in tnames:
#     print(first, last)
# print(tnames[0][0])
# print(tnames[0][1])
# print(tnames[0]


directory = dict(zip((('Cleese', 'John'), ('Aubrey', 'Graham'), ('Icahn', 'Eric'), ('Gilliam', 'Jerry'), ('Jones', 'Terry'), ('Palin', 'Michael')),('098 993 221','029 221 374','388 338 756','098 874 465','983 764 354','563 376 234')))

for first, last in directory:
    print((first, last), " -> " , directory[first, last])