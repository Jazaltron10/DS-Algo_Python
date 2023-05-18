"""
a is a power of b 
if a is divisible by b 

and also a/b is a power of b
"""
"""
Every positive integer that has an exponent of 0 is a power of "1"
and this includes "0" and "1", itself 
"""
"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case
"""
def is_divisible(x,y):
    return  x % y == 0

# print(is_divisible(10,2))


def is_power(a,b):
    if is_divisible:
        print("Hello")
    elif is_divisible(a,b) and is_power(a/b, b):
        print("hello world")
    else:
        print("my name is")
        is_power(a/b , b)
    

is_power(10,2)


# This is some code for the Ackerman Function 
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


Ackerman_Function = ack(3,4)
print(Ackerman_Function)


import math

x = 1
a = 0
while x < 26:
    print("Hello world", x)
    asqrd = math.pow(a+x,2)
    print(asqrd)
    y = abs(math.sqrt(asqrd))
    print("The squareroot of ", asqrd, " is ", y , "\n")
    x +=1






print(abs(29/8.9))
print(int(29/8.9))
print(math.floor(29/8.9))




print("Wk_5_Discussion_Assignment.py")
import math


def my_sqrt(a):
    x = 10
    
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return y

# print(my_sqrt(8))



def test_sqrt():
    a = 1
    while a < 26:
        temp_diff = my_sqrt(a) - math.sqrt(a)
        diff = abs(temp_diff)

        print(f"a = {a}    |    my_sqrt(a) = {my_sqrt(a)}    |    math.sqrt(a) = {math.sqrt(a)}    |    diff = {diff}")
        a +=1


test_sqrt()







# This is the actual discussion assignment

fruit = "banana"
letter = fruit[1]

print(letter)

i = 1

print(len(fruit) ** 2)

last = fruit[i + 4]
print(fruit)
print(last)






def String_Manipulation():
    print("\nreverse\n")
    word = "realmadrid"
    # print(word[-10])


    i = -1
    while i > - (len(word)+1):
        print(word[i])
        i-=1


    print("\nnormal\n")
    r = 0
    while r < len(word):
        print(word[r])
        r+=1




    word_2 = "manchester_city_UCL"

    a = -1
    print("\nreverse\n")
    while a > -(len(word_2)+1):
        print(word_2[a])
        a-=1

    print("\nnormal\n")

    b = 0
    while b < len(word_2):
        print(word_2[b])
        b+=1



# String_Manipulation()


prefixes = 'JKLMNOPQ'
suffix = 'ack'

def robert_series():
    u = "u"
    for l in prefixes:
        if l == 'O' or l == 'Q':
            print(l + u + suffix)
        else:
            print(l + suffix)
        

# robert_series()





fruit = "banana"
print(fruit[:])
print(fruit[:len(fruit)])
print(fruit[1:])

newfruit = "M" + fruit[1:]
print(newfruit)



#Searching for a string
word = input("Please input a word ")
letter = input("Please input a letter ")


def find(word, letter):
    index = 0 
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1  #"Not found"


found = find(word,letter)
# print("The index of the letter found is ", found)
"""This pattern of computation—traversing a sequence and returning when we find what we
are looking for—is called a search."""


target = input("Please input a target ")

# Looping and counting
def count(word, target):
    count = 0 # this keeps track of the number of occurence of a particular string or letter
    
    for letter in word:
        if letter == target:
            count += 1
    print("The letter a occurs ",count, " times in the given word")


count(word, target)


word = "BANANA"

print(word.lower())
print(word.islower())
# Slices return the first but exclude the last = s[n:m] m does not get returned 
n = 10000
count = 0 # type: ignore
while n:
    count = count + 1 # type: ignore
    n = n // 10
print (count)

# fred = "Hello"
# fred[0] = "Y"
# print(fred)


while True:

    while 1 > 0:

        break

    print("Got it!")

    break