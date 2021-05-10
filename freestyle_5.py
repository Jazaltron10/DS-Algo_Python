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
