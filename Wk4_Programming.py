
"""
a is a power of b 
if a is divisible by b 

and also a/b is a power of b
"""

def is_power(a,b):
    print((10 + is_divisible(a,b))*3)
    
    
def is_divisible(x,y):
    return x + y

# is_power(5,6)


#Fermat Theorem 

# a = int(input())
# b = int(input())
# c = int(input())
# n = int(input())

def check_fermat(a,b,c,n):
    if n >= 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")


# check_fermat(a,b,c,n)




# The Triangle
side_a = int(input())
side_b = int(input())
side_c = int(input())

def is_triangle(a, b, c):
    if (a > b + c) and (b < a + c) and (c > a + b):
        print("NO, you can't form a triangle ")
    else: 
        print("YES, a triangle can be formed ")
        
        
is_triangle(side_a, side_b, side_c)


# The Recursion Exercise 
1ZKeJl6tp5!LcW9v