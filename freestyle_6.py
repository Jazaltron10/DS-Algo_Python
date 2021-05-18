print(" THIS WHOLE PYTHON FILE EXPLORES THE LIST DATA STRUCTURE IN PYTHON ")

"""
user_numbers = input()
my_list = user_numbers.split(",")

print(user_numbers)



for i in range(len(my_list)):
    my_list[i] *= 2


print(my_list)
"""



list_1 = [2,4,6,8]
list_1.append(10) # The append method is used to add elements to the end of the list.
for i in range(len(list_1)):
    list_1[i] = list_1[i] * 2
    
    
print(list_1)

# Using the slice operator to modify the contents of a list 
list_1[0:2] = [3, 5]
print(list_1)

list_2 = ['a','b','c','d','e']
list_1.extend(list_2) # This just appends list_2 to the existing list 
print(list_1)

list_3 = [2,4,6,8,-6,-4,-2]
for i in range(len(list_3)):
    list_3[i] = list_3[i] * list_3[i]


print(list_3)
list_3.sort()
# print(abs(list_3))
print(list_3)

print(sum(list_3))


# The reduce Operation
"""
The reduce operation tends to combine a sequence of elements into a single value
"""
t = [54, 62, 93, 17, 31, 65, 23]
print(t)
print(sum(t))


# The map operation
"""
The map operation allows us to traverse a list while building another
"""
l = ['agent','Regent','Urgent','pungent','cogent']

mp = []
cp = []
for s in l:
    mp.append(s.upper())
    if s.islower():
        cp.append(s)
    
# The Filter operation
"""
The filter operation allows us to return some elements as sublist from a list after they have been evaluated by a conditional 
"""

    
print(mp)
print(cp)


# Deleting Elements from a list
# Method 1
mp.pop(1) # if index is not provided it deletes and returns the last element.
print(mp)

# Method 2
del mp[2]        
print(mp)

# Method 3
# This is for when you know the element you want to remove but not the index of the element

mp.remove('COGENT') # the return value from remove is None 
print(mp)

# To remove more than one element, you can use the del with a slice index:
tp = [54, 62, 93, 17, 31, 65, 23]
del tp[1:5] # as usual, the slice selects all the elements up to but not includuing the second index.
print(tp)



print("\n\nTHE LISTS AND STRINGS SECTION")
"""
A LIST is a Sequence of values 
A STRING is a Sequence of characters
To convert a String to a List of characters, which are not the 
same thing, we use list().

"""


st = 'jonathan'
los = list(st)

print(st)
print(los)


# TO break a string into words you can use the split method
sen = 'Cristiano is the best in the world'
ls = sen.split()
print(ls)

"""
DELIMITER:
This is an optional argument that specifies which characters to use a word boundaries. example you can use a hyphen as a delimiter '-'
Example:
"""

egg = 'spam-spam-spam-spam-jam'
delimiter = '-'
keg = egg.split(delimiter)
print(keg)

"""
THE JOIN METHOD 
this is the inverse of the split Method. 
it takes a list of strings and concatenates the elements.
Join is a string method,
So you have to invoke it on the delimeter and pass the list as a parameter
Example
"""

delimeter = '/' # here the delimeter is a forward slash, it can be any character at all
weg = delimeter.join(keg)
print(weg)
meg = '+++++'.join(keg)
print(meg)



"""
OBJECTS AND VALUES
To check whether two variables refer to the same object, you can use the is operator.
"""

a = 'banana'
b = 'banana'

print(a is b)
"""
In this example python only created one string object, and both a and b refer to it.
But when you create two lists, you get two objects:
"""






