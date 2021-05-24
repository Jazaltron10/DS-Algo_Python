print("Discussion Assignment")
"""
Meant to describe how tuples can be useful with loops over lists and Dictionaries
When it comes to loops
for lists, it is the elements in the lists that is iterated over or looped through. 
While for dictionaries it is the keys that get iterated over and not the values. 
With tuples both the index and elements of the sequence can be
looped through and this gives the programmer flexibility to add logic to either one.
Below are code snippets that show how the use of the tuple, for loop and various methods
and functions can bring a whole new functionality to traversing lists and dictionaries.
"""

# We can explore the usefulness of loops using a tuple with the zip function
print("\nThe zip function")
"""
One of the major functionality the tuple gives with for loops is the ability to traverse
two list or dictionary while reassigning their values, and this is achieved using the
zip function.
So Basically combining the power of the zip function and a for loop i have been able to use
tuple reassignment to reassign the values of two lists, two strings, and two dictionaries. 
Because the zip function is an iterator and produces a tuple, this means that all the contents
within this tuple can be traversed using a loop.
"""
list_10 = ['a', 'b', 'c', 'd', 'e']
list_20 = ['apple', 'B', 'cow', 'D', 'e']
list_30 = ['apple', 'bee', 'corn', 'dogs', 'enter']
list_40 = [1,2,3,4,5,6,7,8,9]
dic_5 = dict(zip(['ronaldo', 'messi', 'benzema','ramos','lewandowski'],[5,6,0,0,1]))
dic_6 = dict(zip(['Kylian', 'Felix', 'Haaland','Sterling','Vinicius'],[5,6,0,0,1])) 


def reassign(t1,t2):
    for x , y in zip(t1,t2):
        print(y , x)
        

reassign('james','john')
reassign(list_10, list_20)
reassign('zicko','annabel')
reassign(list_30, list_40)            
reassign(dic_5,dic_6)        

"""
So with tuples and the zip function, you can loop or traverse over two lists or dictionaries
at the same time and also perform some value reassignment if you want to.
"""


print("\nThe enumerate function")
"""
For both a list and a dictionary you can only traverse through their values and keys
respectively but with the built-in function enumerate and the use of tuple both the
index and the elements can be traversed.
Most Sequence in python if not all are Zero indexed and with the enumerate function
when traversing through multiple sequence we get to see this(Downey, 2015).
And if you decide to traverse through only the index and print it,
what gets printed is stil a tuple of the index and the element.
"""
def enum_func():
    print('\n')
    for index in enumerate('John Bond'):
        print(index)# strings
    print('\n')
    for index, element in enumerate(['f','g','h','i','j']):
        print(index, element)   # lists
    print('\n')
    for index, element in enumerate((1,2,3,4,5)):
        print(index, element)   # tuples
    print('\n')
    for index, element in enumerate({'a':"apple",'b':"ball",'c':"cat",'d':"Dog"}):
        print(index, element)   # dictionaries
    print('\n')
    
enum_func()

"""
So with the tuple and the enumerate function when iterating over a list or dictionary
the loop traverses over both the index as well as the elements in each respective sequence.
"""



print("\nThe items method")
"""
With the items method the key and value are presented in the form of a tuple and can be
traversed with a loop, because the items method is a method that
returns a sequence of tuples,where each tuple is a key-value pair this
results in a dict_items object which is an iterator like the zip object
and it iterates the key-value pairs(Downey, 2015).
Further operations can be performed on all key-value pairs simultaneously in the loop.
Now if you try to loop through the dictionary without the items method
you get a ValueError like this:
ValueError: not enough values to unpack (expected 2, got 1)     
"""    
dicki = dict(zip(('X', 'Y', 'Z'),('Albert','Bonquino','Carter'))) # tuple -> tuple
print(dicki)
for key, value in dicki.items():
    newval = value.upper()
    newkey = key.lower()
    print(newkey, newval)
    
    
    
"""
Please I have attached my python source code to my submission feel free to run it 
References:
Downey, A. (2015). Think Python: How to think like a computer scientist. 
Green Tea Press. https://my.uopeople.edu/mod/page/view.php?id=241793
"""    
    
    
    
